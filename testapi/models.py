from django.db import models

# Create your models here.
class Student(models.Model):
    hoten = models.CharField(max_length=30)
    tuoi = models.IntegerField(default=10)
    gioitinh = models.CharField(max_length=5)

    def __str__(self):
        return(self.hoten)