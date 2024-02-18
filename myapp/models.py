from django.db import models

# Create your models here.

class Post(models.Model):
    message = models.CharField(max_length=1000)
    create_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.message