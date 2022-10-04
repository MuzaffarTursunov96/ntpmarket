from distutils.command.upload import upload
from email.policy import default
from django.db import models
from datetime import datetime
from accounts.models import User
import jsonfield

# Create your models here.

class Projects(models.Model):
  name = models.CharField(max_length=255)
  slug = models.CharField(max_length=255)
  liked = models.BooleanField(default=False)
  likes = models.IntegerField(default=0)
  description = models.TextField(default="")
  image = models.ImageField(upload_to='images/',blank=True,null=True)
  price = models.FloatField(default=0)
  time_left = models.CharField(max_length=50,default=str(datetime.now()))
  creator = models.ForeignKey(User, on_delete=models.PROTECT)
  collection = models.ForeignKey('Collection',on_delete=models.PROTECT,blank=True,null=True)
  biddings = jsonfield.JSONField(default=[])
  bought = models.IntegerField(default=0)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.name

class Collection(models.Model):
  name =models.CharField(max_length = 255)
  avatar = models.ImageField(upload_to = 'collections/',blank=True,null=True ,default='images/example.jpg')
  def __str__(self):
    return self.name

class History(models.Model):
  project = models.ForeignKey(Projects, on_delete = models.PROTECT)
  date = models.DateTimeField(default=datetime.now, blank=True,null=True)
  price =models.FloatField(default=0)

class Image(models.Model):
  name = models.ImageField(upload_to ='images/')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  def __str__(self):
    return str(self.name)

class Wishlist(models.Model):
  user = models.ForeignKey(User,on_delete=models.PROTECT)
  project = models.ForeignKey(Projects,on_delete=models.PROTECT)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

class UserBiddings(models.Model):
  user = models.ForeignKey(User,on_delete=models.PROTECT)
  project = models.ForeignKey(Projects,on_delete=models.PROTECT)
  price = models.IntegerField(default = 0)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
