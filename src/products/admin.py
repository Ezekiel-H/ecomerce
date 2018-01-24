from django.contrib import admin

# Register your models here.

from .models import Product, Supplier, Region, Varietal

class ProductAdmin(admin.ModelAdmin):
	list_display = ['__str__', 'slug']
	class Meta:
		model = Product


admin.site.register(Product, ProductAdmin)

admin.site.register(Supplier)
admin.site.register(Region)
admin.site.register(Varietal)
