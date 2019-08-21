from django.contrib import admin
from .models import Distributor

# Register your models here.
@admin.register(Distributor)

#This will show the attributes of the objects in the admin view
class DistributorAdmin(admin.ModelAdmin):
    list_display = ['name']
