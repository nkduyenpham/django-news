from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    content = models.TextField()
    post_date = models.DateField(null=True)

    def __str__(self): #set up how it display inside the database of django admin
        return f"{self.title}"