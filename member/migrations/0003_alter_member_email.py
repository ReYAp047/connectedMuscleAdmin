# Generated by Django 3.2 on 2022-05-03 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0002_auto_20220504_0055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='Email',
            field=models.CharField(max_length=512),
        ),
    ]
