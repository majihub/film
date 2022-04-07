from django.db import models

# Create your models here.
class movie(models.Model):
    name=models.CharField(max_length=250)
    desc=models.TextField()
    year=models.IntegerField()
    director=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pic')
    def __str__(self):
        return self.name