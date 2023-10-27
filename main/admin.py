from django.contrib import admin
from .models import (
    Category, Collection,
    Product, TrandyProduct,
    StayUpdated, OurShop,
    BillingAddress, ShippingAddress,
    ContactUs , GeneralSlider
)




admin.site.register(Category)
admin.site.register(Collection)
admin.site.register(Product)
admin.site.register(TrandyProduct)
admin.site.register(StayUpdated)
admin.site.register(OurShop)
admin.site.register(BillingAddress)
admin.site.register(ShippingAddress)
admin.site.register(ContactUs)
admin.site.register(GeneralSlider)
