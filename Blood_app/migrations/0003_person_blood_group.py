# Generated by Django 5.0.6 on 2024-06-30 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blood_app', '0002_rename_divison_person_division'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='blood_group',
            field=models.CharField(max_length=10, null=True),
        ),
    ]