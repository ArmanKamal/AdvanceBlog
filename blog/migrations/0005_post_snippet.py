# Generated by Django 3.0.7 on 2020-10-30 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20201030_0045'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='Add a snippet', max_length=255),
        ),
    ]
