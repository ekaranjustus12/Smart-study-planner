# Generated by Django 2.1.4 on 2019-01-03 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studyplanner', '0013_auto_20190103_0846'),
    ]

    operations = [
        migrations.AddField(
            model_name='path',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='plan',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='subject',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='subtopic',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
