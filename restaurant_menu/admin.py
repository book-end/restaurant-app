from django.contrib import admin
from .models import Item

# Register your models here.

# shows list of items on interface when added
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ("meal","status")
    list_filter = ("status",)
    search_fields = ("meal", "description")

admin.site.register(Item, MenuItemAdmin)