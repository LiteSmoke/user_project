# Generated by Django 3.1.4 on 2020-12-24 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0005_auto_20201224_0949'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='profile_icon',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]