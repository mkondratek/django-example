# Generated by Django 3.1.4 on 2021-01-10 14:22

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('notes', '0006_topic_is_public'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Topic',
        ),
    ]
