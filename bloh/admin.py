from django.contrib import admin
from .models import Addermodel,AreaCategorymodel,Commentarticle
# Register your models here.
@admin.register(Addermodel)
class Addadmin(admin.ModelAdmin):
    list_display=('name','author','wdate','udate')
    search_fields=('name','author')

@admin.register(AreaCategorymodel)
class AreaAdmin(admin.ModelAdmin):
    list_display=('name','population','economic_region')

@admin.register(Commentarticle)
class Commentadmin(admin.ModelAdmin):
    list_display=('author','wdate','entry')
    search_fields=['name']
