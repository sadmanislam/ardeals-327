from django.contrib import admin
from . models import Deal
from . models import User
from . models import Area
from . models import Category, Type

admin.site.register(Deal)
#admin.site.register(User)
admin.site.register(Area)
admin.site.register(Category)
admin.site.register(Type)

# Register your models here.
