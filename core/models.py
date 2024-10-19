from django.db import models

# Create your models here.

class Player(models.Model):
    picture = models.ImageField(upload_to="uploads/", blank=True, null=True)
