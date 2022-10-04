from django.contrib import admin

from projects.models import *

# Register your models here.
admin.site.register(Projects)
admin.site.register(Collection)
admin.site.register(History)
admin.site.register(Image)
admin.site.register(UserBiddings)
admin.site.register(Wishlist)
