from django.contrib import admin
from django.contrib.admin import ModelAdmin
from . import models


class UserAdmin(ModelAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_active')
    search_fields = ('username', 'email')
    list_filter = ('is_staff', 'is_active')


class DocumentAdmin(ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title', 'content')
    list_filter = ('created_at', 'updated_at')


admin.site.register(models.User, UserAdmin)
admin.site.register(models.Document, DocumentAdmin)
admin.site.site_header = "Manadoc Admin"
admin.site.site_title = "Manadoc Administration"
admin.site.index_title = "Welcome to Manadoc Admin"
