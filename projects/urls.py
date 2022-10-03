from django.urls import path, include
from .views import *

urlpatterns = [
path('assets/<slug>', AssetApiView.as_view() , name='asset-single'),
path('assets/projects/all/', AssetAllApiView.as_view() , name='asset-all'),
path('submit/', AssetBid.as_view() , name='submit'),
path('collection/', CollecionsApiView.as_view() , name='collection'),
path('add/',AssetCreateApiView.as_view(),name='add'),
path('delete-asset/<int:pk>/',AssetDelete.as_view(),name='delete'),
path('wishlist/add/',WishlistAdd.as_view(),name='wishlist-add'),
path('wishlist/remove/',WishlistDelete.as_view(),name='wishlist-revome'),
path('wishlist/get',WishlistAll.as_view(),name='wishlist-all'),

]
