# Generated by Django 2.0.6 on 2018-07-04 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20180702_2009'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='sexual_pref',
            field=models.CharField(choices=[('A', 'Heterosexual'), ('B', 'Bisexual'), ('C', 'Homosexual'), ('D', 'Sapiosexual')], default='A', max_length=1),
            preserve_default=False,
        ),
    ]
