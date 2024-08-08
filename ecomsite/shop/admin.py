from django.contrib import admin
from .models import Product,Order

# Register your models here.
admin.site.site_header = "E-commerce Site"
admin.site.site_title = "Ecom-site"
admin.site.index_title = "Manage ecom-site"

class ProductAdmin(admin.ModelAdmin):

    def change_category_to_default(self,request,queryset):
        queryset.update(category="default")

    change_category_to_default.short_description = 'Default category'
    list_display = ('title','price','discount_price','category',)
    search_fields = ('category',)
    actions = ('change_category_to_default',)
    fields = ('title','price',)
    list_editable = ('price','discount_price',)

admin.site.register(Product,ProductAdmin)
admin.site.register(Order)