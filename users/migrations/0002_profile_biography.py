# Generated by Django 2.1.7 on 2019-03-02 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='biography',
            field=models.TextField(blank=True, null=True),
        ),
    ]
