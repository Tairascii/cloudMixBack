# Generated by Django 4.2.7 on 2023-11-22 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chat',
            old_name='bot_id',
            new_name='bot',
        ),
        migrations.RenameField(
            model_name='chat',
            old_name='user_id',
            new_name='user',
        ),
    ]