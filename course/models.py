from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db.models.fields import EmailField

class subject(models.Model):
    area=models.CharField(max_length=200)
    def __str__(self):
        return self.area    

class teacher(models.Model):
    name=models.ForeignKey(User, on_delete= models.CASCADE)
    area=models.ManyToManyField(subject)
    description=RichTextField()
    

class course(models.Model):
    title=models.CharField(max_length=500)
    areas=models.ManyToManyField(subject)
    description=RichTextField()
    instructor=models.ForeignKey(teacher, on_delete= models.CASCADE)
    material=models.CharField(max_length=1000)

    def __str__(self):
        return self.title

class userDetail(models.Model):
    username=models.CharField(max_length=50)
    name=models.CharField(max_length=100)
    email=models.EmailField()
    dob=models.DateField()
    join_date=models.DateField()
    city=models.CharField(max_length=30)
    state=models.CharField(max_length=30)
    about=RichTextField()
    def __str__(self):
        return self.name

class teacher_app(models.Model):
    username=models.CharField(max_length=50)
    name=models.CharField(max_length=100)
    email=models.EmailField()
    dob=models.DateField()
    join_date=models.DateField()
    city=models.CharField(max_length=30)
    state=models.CharField(max_length=30)
    about=RichTextField()
    def __str__(self):
        return self.name

class userCourse(models.Model):
    id=models.AutoField(primary_key=True)
    un=models.CharField(max_length=2000)
    idn=models.CharField(max_length=200)
    nm=models.CharField(max_length=200)
    def __str__(self):
        return self.nm

class certificate(models.Model):
    course=models.CharField(max_length=500)
    name=models.CharField(max_length=500)
    def __str__(self):
        return self.name





