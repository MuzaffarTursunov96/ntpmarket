from dataclasses import fields
from pyexpat import model
from rest_framework.response import Response
from rest_framework import serializers
from .models import *
from datetime import datetime,timezone



class ImageMixin:
  def get_image(self,project):
    ids =project.image.split(',')
    img_links=[]
    if len(ids)>1:
      for id in ids:
        if Image.objects.filter(id = int(id)).exists():
          link = str(Image.objects.filter(id = int(id)).first().name)
          img_links.append(link)
    elif len(ids) == 1:
      if len(ids[0]) > 0:
        if Image.objects.filter(id = int(ids[0])).exists():
          link = str(Image.objects.filter(id = int(ids[0])).first().name)
          img_links.append(link)
    return img_links
  
class AssetSerializer(serializers.ModelSerializer,ImageMixin):
  creator = serializers.SerializerMethodField('get_creator') 
  history = serializers.SerializerMethodField('get_history') 
  image = serializers.SerializerMethodField('get_image') 
  # time_left = serializers.SerializerMethodField('get_time_left')
  class Meta:
        model = Projects
        fields =["id","slug","liked","likes","name","image","description","price","time_left","updated_at","creator","collection","history"]
        depth = 1
  
  def get_creator(self,project):
    name =project.creator.username
    avatar =str(project.creator.avatar)
    return {'name':name,'avatar':avatar}

  def get_history(self,project):
    histories =History.objects.filter(project=project)
    total = len(histories)
    data = []
    for history in histories:
      data.append({'date':history.date,'price':history.price})
    return{"total":total,'data':data}

  

class AssetsAllSerializer(serializers.ModelSerializer,ImageMixin):
  image = serializers.SerializerMethodField('get_image') 
  # time_left = serializers.SerializerMethodField('get_time_left')
  class Meta:
    model = Projects
    fields =["id","name","liked","likes","slug","image","price","time_left","biddings"]

class CollectionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Collection
    fields ="__all__"  

class CreateAssetSerializer(serializers.ModelSerializer):
  class Meta:
    model = Projects
    fields = ["name","slug","image","price","time_left","collection","creator"]