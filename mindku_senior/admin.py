from django.contrib import admin

from .models import *


admin.site.site_header = "MindKU Senior Admin"
admin.site.site_title = "Admin Portal"


class CompanyUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'name', 'phone', 'address']
    list_display_links = ['id', 'email', 'name', 'phone', 'address']
    search_fields = ['email', 'name']
    
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'name', 'birth', 'gender', 'phone', 'address']
    list_display_links = ['id', 'email', 'name', 'birth', 'gender', 'phone', 'address']
    search_fields = ['email', 'name']




admin.site.register(CompanyAdmin)
admin.site.register(CompanyUser, CompanyUserAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Question_depression)
admin.site.register(Question_anxiety)
admin.site.register(Question_vitality)
admin.site.register(Question_suicide)
admin.site.register(Report)
