# Generated by Django 5.0.6 on 2024-07-02 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blood_app', '0003_person_blood_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='person_image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
