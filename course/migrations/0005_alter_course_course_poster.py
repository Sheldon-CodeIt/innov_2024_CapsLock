# Generated by Django 4.2.1 on 2024-02-27 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_alter_course_course_poster'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_poster',
            field=models.ImageField(blank=True, null=True, upload_to='course/static/course_posters/'),
        ),
    ]
