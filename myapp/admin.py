from django.contrib import admin
from .models import Members,Platform,Product,ProductPrice, Item,ItemPrice,Contact

# Register your models here

admin.site.register(Members)
admin.site.register(Platform)
admin.site.register(Product)
admin.site.register(ProductPrice)
admin.site.register(Item)
admin.site.register(Contact)

admin.site.register(ItemPrice)
