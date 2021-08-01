from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models

# Create your models here.
from django.db.models import CASCADE


class Course(models.Model):
    name=models.CharField(max_length=30 , null=False)
    slug=models.CharField(max_length=100 , null=False , unique=True)
    short_description=models.CharField(max_length=100, null=True ,blank=True)
    description=models.TextField()
    price=models.IntegerField(null=False)
    discount=models.IntegerField(null=False , default=0)
    active=models.BooleanField(default=False)
    thumbnail=models.ImageField(upload_to="thumbnail")
    date=models.DateTimeField(auto_now_add=True)
    resource=models.FileField(upload_to="resource")
    length=models.IntegerField(null=False)
    def __str__(self):
        return self.name


class CourseProperty(models.Model):
    description = models.CharField(max_length=250 , null=True , blank=True)
    Course = models.ForeignKey(Course , on_delete=models.CASCADE , null=False)

    class Meta:
        abstract = True;

class Tag(CourseProperty):
    pass

class Prerequisite(CourseProperty):
    pass

class Learning(CourseProperty):
    pass


class Video(models.Model):
    title = models.CharField(max_length=250 , null=False , blank=False)
    videodesc=models.TextField(null=True ,blank=True)
    Course = models.ForeignKey(Course , on_delete=models.CASCADE , null=False)
    serial_number = models.IntegerField(null= False)
    video_id=models.CharField(max_length=250 ,null=False)
    is_preview=models.BooleanField(default=False)
    def __str__(self):
        return self.title



class Contact(models.Model):
    name=models.CharField(max_length=250,null=True)
    email =models.EmailField(null=True)
    phone=models.CharField(max_length=20 , null=True)
    message=models.TextField()
    Timestamp=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name


class MyProfile(models.Model):
    name = models.CharField(max_length = 100)
    user = models.OneToOneField(to=User, on_delete=CASCADE)
    age = models.IntegerField(default=18, validators=[MinValueValidator(18)])
    city=models.CharField(max_length=250,null=True,default="")
    zipcode=models.CharField(max_length=250 , null=True)
    address = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=20, default="single", choices=(("single","single"), ("married","married"), ("widow","widow"), ("seprated","seprated"), ("commited","commited")))
    gender = models.CharField(max_length=20, default="female", choices=(("male","male"), ("female","female")))
    phone_no = models.CharField(max_length=15, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    pic=models.ImageField(upload_to = "uploads", null=True)

    def __str__(self):
        return "%s" % self.user





