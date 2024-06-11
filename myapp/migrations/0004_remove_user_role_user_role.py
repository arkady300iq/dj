# Generated by Django 5.0.6 on 2024-06-11 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_user_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='role',
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.ManyToManyField(to='myapp.role'),
        ),
    ]
