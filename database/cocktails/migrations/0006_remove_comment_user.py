# Generated by Django 2.0 on 2017-12-20 17:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cocktails', '0005_comment_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
    ]
