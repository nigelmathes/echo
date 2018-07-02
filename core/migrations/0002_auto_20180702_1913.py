# Generated by Django 2.0.6 on 2018-07-02 19:13

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='echo',
            old_name='owner',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='echo',
            name='audio',
            field=models.FileField(upload_to=core.models.echo_directory),
        ),
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.FileField(blank=True, null=True, upload_to=core.models.profile_directory),
        ),
    ]