from django.db import models
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    COURSE_LEVEL_CHOICES = [
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('advanced', 'Advanced'),
    ]

    course_id = models.AutoField(primary_key=True)
    course_title = models.TextField(default='title')
    course_description = models.TextField()
    course_author = models.TextField(default="author")
    course_outcomes = models.TextField()
    course_tags = models.CharField(max_length=100)
    course_level = models.CharField(max_length=20, choices=COURSE_LEVEL_CHOICES)
    course_poster = models.ImageField(upload_to='course/static/course_posters/', null=True, blank=True)

    def __str__(self):
        return f"Course ID: {self.course_id}, Description: {self.course_description[:50]}"
    

from django.db import models
from django.utils import timezone

class Video(models.Model):
    CATEGORY_CHOICES = [
        ('frontend', 'Frontend'),
        ('backend', 'Backend'),
        ('app', 'App'),
        ('gamedev','Game Development'),
        ('devops','Devops')
    ]

    vid_id = models.AutoField(primary_key=True)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    vid_title = models.CharField(max_length=255)
    vid_description = models.TextField()
    vid_embedded_url = models.TextField()
    likes = models.BooleanField(default=False)
    playlist = models.BooleanField(default=False)
    notes = models.TextField()
    published_date = models.DateTimeField(default=timezone.now)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    video_tags = models.CharField(max_length=100)
    vid_duration = models.CharField(max_length=20)  # Assuming duration format like "HH:MM:SS"

    def __str__(self):
        return self.vid_title

class LikedVideo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    video = models.ForeignKey('Video', on_delete=models.CASCADE)
    liked_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} likes {self.video.vid_title}"

class WatchLaterVideo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    video = models.ForeignKey('Video', on_delete=models.CASCADE)
    added_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} added {self.video.vid_title} to watch later"
    


class ChatBot(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="GeminiUser", null=True
    )
    text_input = models.CharField(max_length=500)
    gemini_output = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.text_input