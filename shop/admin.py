from django.contrib import admin
from . models import Product, Order

# Register your models here.

admin.site.site_header = "E-commerce site"
admin.site.site_title  = "Dilbis Shoping Cart"
admin.site.index_title = "Dilbis Shopping"

class ProductAdmin(admin.ModelAdmin):


    list_display = ("title", "price", "discount_price", "category")  # displays these products in admin/product page...
    search_fields = ('category',)    # search accoding to category in admin/product page...

    # adding acitons to the admin/product page...
    def change_category(self, request, queryset):
        queryset.update(category="dilbis")
        
    change_category.short_description = 'Default Category'
    actions = ('change_category',)

    # Displaying certain items to admin/products/name_product...
    # fields=('title', 'price',)

    # Making list item editable
    list_editable = ('price', 'category',)

    



admin.site.register(Product, ProductAdmin)
admin.site.register(Order)