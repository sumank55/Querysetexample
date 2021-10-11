from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    roll=models.IntegerField(unique=True)
    address=models.CharField(max_length=200)
    marks=models.IntegerField()
    pass_date=models.DateField()

    def __str__(self):
        return self.name

    def __str__(self):
        return '%s %s' % (self.name, self.roll)




class Teacher(models.Model):
    name=models.CharField(max_length=100)
    empnum=models.IntegerField(unique=True,null=True)
    address=models.CharField(max_length=200)
    salary=models.IntegerField()
    join_date=models.DateField()

    def __str__(self):
        return self.name