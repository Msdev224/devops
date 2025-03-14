from django.contrib import admin
from .models import Category
from unfold.admin import ModelAdmin as UnfoldModelAdmin

# Register your models here.
class CategoryAdmin(UnfoldModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)}

admin.site.register(Category, CategoryAdmin)
