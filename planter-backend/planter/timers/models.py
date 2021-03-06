from django.db import models
from profiles.models import Profile
# signals 
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class Timer(models.Model):
    # signals - create timer model when user profile created 
    @receiver(post_save, sender=Profile)
    def create_timer_for_new_profile(sender, created, instance, **kwargs):
        if created:
            timer = Timer(profile=instance)
            timer.save()
    # Use foreign key to give flexibility 
    profile = models.ForeignKey(Profile, related_name='timers', on_delete=models.CASCADE)
    focus_time = models.IntegerField(default=25*60)
    break_time = models.IntegerField(default=5*60) 
    is_started = models.BooleanField(default=False)
    current_focus_time = models.IntegerField(default=25*60)
    current_break_time = models.IntegerField(default=5*60)

    current_cycle = models.CharField(max_length=20, default='Focus')
    completed_focus_minutes = models.IntegerField(default=0)
    # logged_focus_minutes = models.IntegerField(default=0)

    def __str__(self):
        return "%s's timer" % self.profile.account.username