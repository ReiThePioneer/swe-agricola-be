# Generated by Django 4.2.1 on 2023-06-05 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gameplay', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='boardposition',
            old_name='player_id',
            new_name='board_id',
        ),
        migrations.RenameField(
            model_name='boardposition',
            old_name='position_name',
            new_name='position_type',
        ),
        migrations.RenameField(
            model_name='fenceposition',
            old_name='board_id',
            new_name='position_id',
        ),
    ]
