# Generated by Django 3.2 on 2022-05-04 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='transformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Member_Email', models.EmailField(max_length=254)),
                ('Week_Date', models.DateField()),
                ('Week_Goal', models.CharField(default=False, max_length=512)),
                ('Body_Height', models.FloatField(default=False)),
                ('Body_Weight', models.FloatField(default=False)),
                ('Image_Link', models.URLField()),
            ],
        ),
    ]
