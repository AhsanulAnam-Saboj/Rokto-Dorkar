# Generated by Django 5.0.6 on 2024-07-02 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blood_app', '0005_alter_person_person_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='person_image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]