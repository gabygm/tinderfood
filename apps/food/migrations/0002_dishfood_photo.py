# Generated by Django 2.0.4 on 2018-04-12 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dishfood',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='dishfood/'),
        ),
    ]
