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
path('asset/update',AssetUpdate.as_view(),name='asset-update'),
path('assets/projects/owner',AssetsOwner.as_view(),name='asset-owner'),
path('assets/projects/biddings',OwnerBiddings.as_view(),name='owner-biddings'),
path('item-slug',ProjectSlugs.as_view(),name='project-slugs'),
path('footer-tems',FooterItems.as_view(),name='footer-items'),
path('default-bid',DefaultBidd.as_view(),name='default-bid'),
path('wishlist-check',CheckWishlist.as_view(),name='check-wishlist')
]
