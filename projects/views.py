from email.mime import image
from django.shortcuts import render
from .serializers import *
from rest_framework.generics import RetrieveAPIView,ListAPIView,UpdateAPIView,CreateAPIView,DestroyAPIView
from .models import *
from rest_framework.response import Response 
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework import status
from slugify import slugify
import random
import json
import string
from rest_framework_simplejwt.authentication import JWTAuthentication
# Create your views here.


class AssetPagination(PageNumberPagination):
  page_size = 10
  page_size_query_param = 'page_size'
  max_page_size = 10000

  def get_paginated_response(self, data):
      return Response({
          'next': self.get_next_link(),
          'previous': self.get_previous_link(),
          'count': self.page.paginator.count,
          'colection': data['collection'],
          'search': data['search'],
          'data': data['data']
      })

class AssetApiView(RetrieveAPIView):
  queryset = Projects.objects.all()
  serializer_class =AssetSerializer
  authentication_classes=[JWTAuthentication]
  lookup_url_kwarg ='slug'

  def get(self,request,slug):
    project =Projects.objects.filter(slug=slug).first()
    if request.user.is_authenticated:
      if Wishlist.objects.filter(user =request.user,project=project).exists():
        project.liked=True

    serializer_data=AssetSerializer(project)
    return Response({'date':serializer_data.data})

class AssetAllApiView(ListAPIView):
  queryset = Projects.objects.all()
  serializer_class = AssetsAllSerializer
  pagination_class = AssetPagination

  def get(self,request):
    collection = request.GET.get('collection',None)
    search = request.GET.get('search',None)
    sort = request.GET.get('sort',None)
    if sort:
      if sort =='asc':
        if collection and search:
          col = get_object_or_404(Collection,name=collection)
          data = Projects.objects.filter(name__icontains=search , collection=col).order_by('price')
          if len(data) == 0:
            data = Projects.objects.filter(Q(name__icontains=search) | Q(collection=col)).order_by('price')
        elif search:
          data = Projects.objects.filter(name__icontains=search).order_by('price')
        elif collection:
          col = get_object_or_404(Collection,name=collection)
          data = Projects.objects.filter(collection=col).order_by('price')
        else:
          data =Projects.objects.all().order_by('price')
      elif sort =='desc':
        if collection and search:
          col = get_object_or_404(Collection,name=collection)
          data = Projects.objects.filter(name__icontains=search , collection=col).order_by('-price')
          if len(data) == 0:
            data = Projects.objects.filter(Q(name__icontains=search) | Q(collection=col)).order_by('-price')
        elif search:
          data = Projects.objects.filter(name__icontains=search).order_by('-price')
        elif collection:
          col = get_object_or_404(Collection,name=collection)
          data = Projects.objects.filter(collection=col).order_by('-price')
        else:
          data =Projects.objects.all().order_by('-price')
      elif sort =='new':
        if collection and search:
          col = get_object_or_404(Collection,name=collection)
          data = Projects.objects.filter(name__icontains=search , collection=col).order_by('-created_at')
          if len(data) == 0:
            data = Projects.objects.filter(Q(name__icontains=search) | Q(collection=col)).order_by('-created_at')
        elif search:
          data = Projects.objects.filter(name__icontains=search).order_by('-created_at')
        elif collection:
          col = get_object_or_404(Collection,name=collection)
          data = Projects.objects.filter(collection=col).order_by('-created_at')
        else:
          data =Projects.objects.all().order_by('-created_at')
      elif sort =='popular':
        if collection and search:
          col = get_object_or_404(Collection,name=collection)
          data = Projects.objects.filter(name__icontains=search , collection=col).order_by('bought')
          if len(data) == 0:
            data = Projects.objects.filter(Q(name__icontains=search) | Q(collection=col)).order_by('bought')
        elif search:
          data = Projects.objects.filter(name__icontains=search).order_by('bought')
        elif collection:
          col = get_object_or_404(Collection,name=collection)
          data = Projects.objects.filter(collection=col).order_by('bought')
        else:
          data =Projects.objects.all().order_by('bought')
    else:
      if collection and search:
        col = get_object_or_404(Collection,name=collection)
        data = Projects.objects.filter(name__icontains=search , collection=col)
        if len(data) == 0:
          data = Projects.objects.filter(Q(name__icontains=search))
      elif search:
        data = Projects.objects.filter(name__icontains=search)
      elif collection:
        col = get_object_or_404(Collection,name=collection)
        data = Projects.objects.filter(collection=col)
      else:
        data =Projects.objects.all()
    # return data

    page = self.paginate_queryset(data)
    if page is not None:
        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response({'collection':collection,'search':search,'data':serializer.data})

    serializer = self.get_serializer(data, many=True)
    return Response(serializer.data)


class AssetBid(UpdateAPIView):
  queryset = Projects.objects.all()
  serializer_class = AssetSerializer
  authentication_classes=[JWTAuthentication]
  permission_classes =(permissions.IsAuthenticated,) 
    
  def post(self,request):
    id =request.data['id']
    price =request.data['price']
    project = get_object_or_404(Projects, id =id)
    if project.creator == request.user:
      return Response({'success':False,'msg':"You can't buy own product! "})

    if UserBiddings.objects.filter(user=request.user,project=project).exists():
      return Response({'success':False,'msg':"This item alredy bougth! "})

    bid = project.biddings
    bid.append({'name':request.user.username,'avatar':str(request.user.avatar)})
    project.biddings = bid
    project.bought = project.bought+1
    project.save()

   
    new_project= Projects.objects.create(
      name=project.name,
      slug=project.slug + ''.join(random.choices(string.ascii_lowercase, k=5)),
      description=project.description,
      image=project.image,
      price=project.price,
      creator=request.user,
      collection=project.collection
    )

    history = History.objects.create(date =datetime.now(),price=price,project=project)

    biddings = UserBiddings.objects.create(user = request.user, project=project, price = price)

    return Response({'success':True,'msg':'Congratulations , successfuly bought!'})

class CollecionsApiView(ListAPIView):
  queryset = Collection.objects.all()
  serializer_class =CollectionSerializer

class AssetCreateApiView(CreateAPIView):
  queryset =Projects.objects.all()
  serializer_class =AssetSerializer
  authentication_classes=[JWTAuthentication]
  permission_classes=(permissions.IsAuthenticated,) 

  def post(self,request):
    data=request.data
    data._mutable = True
    data['slug']=slugify(data['name']+''.join(random.choices(string.ascii_lowercase, k=5)))
    data['creator']=request.user.id
    data._mutable = False
    serializer =CreateAssetSerializer(data=data)
    if serializer.is_valid(raise_exception=True):
      serializer.save()
      return Response({'success':True,'msg':status.HTTP_201_CREATED})
    else:
      return Response({'success':True,'msg':status.HTTP_400_BAD_REQUEST})




class AssetDelete(DestroyAPIView):
  queryset =Projects.objects.all()
  authentication_classes=[JWTAuthentication]
  permission_classes =(permissions.IsAuthenticated,) 

  def get(self,request,pk):
    project = get_object_or_404(Projects, id =pk)
    if project.creator == request.user:
      project.delete()
      return Response({'success':True,'msg':"Successfully deleted"})
    else:
      return Response({'success':False,'msg':"You can't delete this item"})

class WishlistAdd(APIView):
  queryset = Wishlist
  authentication_classes=[JWTAuthentication]
  permission_classes =(permissions.IsAuthenticated,) 

  def post(self,request):
    id =request.data['id']
    project = get_object_or_404(Projects, id =id)
    if project.creator == request.user:
      return Response({'success':False,'msg':"You can't add to wishlist your own item!" })
    else:
      project.likes+=1
      project.save()
      Wishlist.objects.create(user=request.user,project=project)
      return Response({'success':True,'msg':"Successfully added to wishlist"})

class WishlistDelete(APIView):
  authentication_classes=[JWTAuthentication]
  permission_classes =(permissions.IsAuthenticated,) 

  def post(self,request):
    id =request.data['id']
    
    if Wishlist.objects.filter(project_id=id,user_id=request.user.id).exists():
      Wishlist.objects.filter(project_id=id,user_id=request.user.id).delete()
      if Projects.objects.filter(id = id).exists():
        project = Projects.objects.filter(id = id).first()
        project.likes -=1
        project.save()
      return Response({'success':True, 'msg':'Successfully removed from wishlist'})
    else:
      return Response({'success':True,'msg':status.HTTP_404_NOT_FOUND})

class WishlistAll(ListAPIView):
  queryset = Projects.objects.all()
  serializer_class = AssetsAllSerializer
  # pagination_class = AssetPagination
  authentication_classes=[JWTAuthentication]
  permission_classes =(permissions.IsAuthenticated,)

  def get(self,request):
    wishlists =Wishlist.objects.filter(user_id=request.user.id)
    project_ids =[]
    for wishlist in wishlists:
      project_ids.append(wishlist.project.id)

    datas =Projects.objects.filter(id__in =project_ids)
    for data in datas:
      data.liked =True

    # page = self.paginate_queryset(datas)
    # if page is not None:
    #     serializer = self.get_serializer(page, many=True)
    #     return self.get_paginated_response({'data':serializer.data})

    serializer = self.get_serializer(datas, many=True)
    return Response(serializer.data)
  
class AssetUpdate(APIView):
  queryset = Projects.objects.all()
  serializer_class = AssetsAllSerializer
  authentication_classes=[JWTAuthentication]
  permission_classes =(permissions.IsAuthenticated,)

  def post(self,request):
    data = request.data
    id =data['id']
    project = get_object_or_404(Projects, id =id)
    if project.creator == request.user:
      project.time_left = data['time_left']
      if data['price']:
        project.price = data['price']
      project.save()
      return Response({'success':True, 'msg':'Successfully updated'})
    else:
      return Response({'success':False, 'msg':"You can't update this item!"})

class AssetsOwner(ListAPIView):
  queryset = Projects.objects.all()
  serializer_class = AssetsAllSerializer
  authentication_classes=[JWTAuthentication]
  permission_classes =(permissions.IsAuthenticated,)

  def get(self,request):
      datas =Projects.objects.filter(creator = request.user)

      # page = self.paginate_queryset(datas)
      # if page is not None:
      #     serializer = self.get_serializer(page, many=True)
      #     return self.get_paginated_response({'data':serializer.data})

      serializer = self.get_serializer(datas, many=True)
      return Response(serializer.data)

class OwnerBiddings(ListAPIView):
  queryset = UserBiddings.objects.all()
  serializer_class = UserBiddingsSerializer
  authentication_classes=[JWTAuthentication]
  permission_classes =(permissions.IsAuthenticated,)

  def get(self,request):
    datas =UserBiddings.objects.filter(user = request.user)

    # page = self.paginate_queryset(datas)
    # if page is not None:
    #     serializer = self.get_serializer(page, many=True)
    #     return self.get_paginated_response({'data':serializer.data})

    # serializer = self.get_serializer(datas, many=True)
    # projects = []
    # for data in datas:
    #   projects.append(data.project)
    serializer = self.get_serializer(datas, many=True)
    return Response(serializer.data)

class UserGetMe(APIView):
  authentication_classes=[JWTAuthentication]
  permission_classes =(permissions.IsAuthenticated,)

  def get(self,request):
    user = request.user
    total_spent=0
    biddings = UserBiddings.objects.filter(user =user)
    for bid in biddings:
      total_spent +=bid.price

    wishlist_count =len(Wishlist.objects.filter(user =user))
    biddings_count =len(biddings)
    assets_count =len(Projects.objects.filter(creator =user))
    return Response({
      'name':user.username,
      'avatar':str(user.avatar),
      'biograph':user.biograph,
      'wishlist_count':wishlist_count,
      'biddings_count':biddings_count,
      'assets_count':assets_count,
      'total_spent':total_spent
    })
