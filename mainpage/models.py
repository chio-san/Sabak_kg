from django.db import models

class Description(models.Model):
    title = models.CharField(max_length=255)
    created_date = models.DateField(auto_now_add=True)
    text = models.TextField()

class Lesson(models.Model):
    name = models.CharField(max_length=255)
    video = models.FileField()
