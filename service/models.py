from django.db import models

# Create your models here.


class userandtopic(models.Model):
    user_name = models.CharField(max_length=50)
    topic = models.CharField(max_length=150)
    user_mail = models.EmailField()
    # user_id = models.


class contentandtimeperTopic(models.Model):
    topic = models.CharField(max_length=150)
    content_text = models.TextField()
    publish_time = models.TimeField()
    

