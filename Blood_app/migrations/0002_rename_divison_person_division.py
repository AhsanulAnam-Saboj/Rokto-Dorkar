# Generated by Django 5.0.6 on 2024-06-30 07:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blood_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='divison',
            new_name='division',
        ),
    ]