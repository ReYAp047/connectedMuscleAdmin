# Generated by Django 3.2 on 2022-05-04 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0003_alter_member_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='Email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='member',
            name='Member_Name',
            field=models.EmailField(max_length=254),
        ),
    ]
