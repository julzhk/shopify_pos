from django.contrib import admin
from inventory.models import Inventory
from django.utils.html import mark_safe


class InventoryAdmin(admin.ModelAdmin):
    fields = ['image_tag']
    readonly_fields = ['image_tag']
    list_display = ['title','image_tag',]


admin.site.register(Inventory, InventoryAdmin)