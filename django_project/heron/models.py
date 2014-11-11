from django.db import models

# Create your models here.

class Feedback(models.Model):
	body = models.TextField()
	created = models.DateTimeField(auto_now_add=True)