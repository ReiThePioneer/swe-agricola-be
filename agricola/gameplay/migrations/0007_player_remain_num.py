# Generated by Django 4.2.1 on 2023-06-03 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameplay', '0006_actionbox_is_occupied'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='remain_num',
            field=models.IntegerField(null=True),
        ),
    ]
