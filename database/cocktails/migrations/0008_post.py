# Generated by Django 2.0 on 2017-12-20 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cocktails', '0007_auto_20171220_1851'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=120)),
                ('cocktail', models.CharField(max_length=120)),
                ('comment', models.CharField(max_length=120)),
            ],
        ),
    ]
