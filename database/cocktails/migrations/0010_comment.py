# Generated by Django 2.0 on 2017-12-21 05:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cocktails', '0009_auto_20171221_0047'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('likes', models.CharField(max_length=6)),
                ('dislikes', models.CharField(max_length=6)),
                ('comment', models.CharField(max_length=3000)),
                ('date', models.CharField(max_length=100)),
                ('cocktail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cocktails.Cocktail')),
            ],
        ),
    ]
