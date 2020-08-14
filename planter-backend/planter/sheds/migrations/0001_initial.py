# Generated by Django 3.0.6 on 2020-08-14 22:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tools', '0001_initial'),
        ('plants', '0001_initial'),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plant_Shed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity_in_shed', models.IntegerField()),
                ('plant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plants.Plant')),
            ],
        ),
        migrations.CreateModel(
            name='Shed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plant', models.ManyToManyField(through='sheds.Plant_Shed', to='plants.Plant')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Tool_Shed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity_in_shed', models.IntegerField()),
                ('shed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sheds.Shed')),
                ('tool', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tools.Tool')),
            ],
        ),
        migrations.AddField(
            model_name='shed',
            name='tool',
            field=models.ManyToManyField(through='sheds.Tool_Shed', to='tools.Tool'),
        ),
        migrations.AddField(
            model_name='plant_shed',
            name='shed',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sheds.Shed'),
        ),
    ]
