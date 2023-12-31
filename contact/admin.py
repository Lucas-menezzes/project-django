from django.contrib import admin
from contact import models

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'last_name', 'phone', 'email'
    ordering = '-id',
    #list_filter = 'created_date'
    search_fields = 'first_name', 'last_name', 'id'
    list_per_page = 10
    list_max_show_all = 20
    list_editable= 'last_name', 'phone'
    list_display_links= ['id', 'first_name']

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'name',
    ordering = '-id',