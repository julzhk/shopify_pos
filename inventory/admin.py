from django.contrib import admin

from inventory.models import Inventory, Variant


class InventoryAdmin(admin.ModelAdmin):
    fields = ['image_tag']
    readonly_fields = ['image_tag']
    list_display = ['title', 'image_tag', 'available']


class VariantAdmin(admin.ModelAdmin):
    pass


admin.site.register(Variant, VariantAdmin)
admin.site.register(Inventory, InventoryAdmin)
