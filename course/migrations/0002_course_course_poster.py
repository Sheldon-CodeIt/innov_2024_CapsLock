# Generated by Django 4.2.1 on 2024-02-27 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_poster',
            field=models.ImageField(blank=True, null=True, upload_to='course_posters/'),
        ),
    ]