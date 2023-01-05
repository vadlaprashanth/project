from django.contrib import admin
from .models import Locations, Departments, Categories, SubCategories, SKUdata

# Register your models here.
admin.register(Locations)
admin.register(Departments)
admin.register(Categories)
admin.register(SubCategories)
admin.register(SKUdata)