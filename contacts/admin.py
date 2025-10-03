from django.contrib import admin
from .models import Category, Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'phone', 'email', 'created_at', 'category', 'visible')

    list_display_links = ('id', 'first_name', 'last_name')
    list_per_page = 10
    search_fields = ('first_name', 'last_name', 'phone')
    list_editable = ('phone', 'visible')


admin.site.register(Category)
admin.site.register(Contact, ContactAdmin)
