from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class AcceptedpostManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=True)

class Catagory(models.Model):
    catagoryName = models.CharField(max_length=50 ,default="")

    def __str__(self):
          return self.catagoryName


class post(models.Model):
    post_id= models.AutoField(primary_key=True)
    title = models.CharField(max_length=255 ,default="")
    author =models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.CharField(max_length=130, unique=True)
    catagory = models.ForeignKey(Catagory, on_delete=models.CASCADE)
    timeStamp = models.DateTimeField(auto_now_add=True,blank=True)
    thumbnail = models.ImageField(upload_to='shop/images', default="")
    status=models.BooleanField(default="True")

    content = models.TextField()
    acceptpost = AcceptedpostManager()
    objects =models.Manager()

    def __str__(self):
        return self.title

    @property
    def post_idd(self):
        return self.post_id

    @property
    def post_catagory(self):
        return self.catagory.catagoryName

    @property
    def post_author(self):
        return self.author.username