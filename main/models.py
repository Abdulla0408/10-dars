from django.db import models

# Create your models here.


class Teacher(models.Model):
    full_name = models.CharField(max_length=100)
    age = models.IntegerField()
    english_certificate = models.BooleanField()
    phone = models.CharField(max_length=13)

    def __str__(self):
        return self.full_name