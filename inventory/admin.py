from django.contrib import admin

from inventory.models import Inventory


class InventoryAdmin(admin.ModelAdmin):
    fields = ['image_tag']
    readonly_fields = ['image_tag']
    list_display = ['title', 'image_tag', ]


admin.site.register(Inventory, InventoryAdmin)
