# Generated by Django 3.0.7 on 2020-11-03 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20201103_0820'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='phone_num',
            field=models.CharField(blank=True, default='111', max_length=120, null=True),
        ),
    ]