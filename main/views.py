from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import generic
from .models import *
from .forms import *

class HomePageListView(generic.ListView):
    template_name = 'index.html'


    @staticmethod
    def __extract_all_data():
        categories = Category.objects.all()
        collections_right = Collection.objects.all()[:1]
        collections_left = Collection.objects.all()[1:]
        trandy_products = TrandyProduct.objects.get().products.all()
        general_slider_active = GeneralSlider.objects.first()
        general_slider = GeneralSlider.objects.all()[1:]

        just_arrived = Product.objects.order_by('-data_time')[:8]


        for product in trandy_products:
            product.discount_price = round(product.price * (1 - product.discount / 100), 2)

        for product in just_arrived:
            product.discount_price = round(product.price * (1 - product.discount / 100), 2)


        context = {
            'navbar': 'home',
            'categories': categories,
            'collections_left': collections_left,
            'collections_right': collections_right,
            'trandy_products': trandy_products,
            'general_slider':general_slider,
            'general_slider_active':general_slider_active,
            'just_arrived':just_arrived,
        }

        return context

    def get(self, request):

        context = self.__extract_all_data()

        return render(request, self.template_name, context)
    
    def post(self, request):
        form = StayUpdatedForm(request.POST)

        if form.is_valid():
            form.save()
        else:
            form = StayUpdatedForm()
        
        context = self.__extract_all_data()
        context.update({'form':form})

        return render(request, self.template_name, context)


class CartPageListView(generic.ListView):
    template_name = 'cart.html'

    def get(self, request):

        context = {
            'navbar': 'cart',
        }

        return render(request, self.template_name, context)
    

class CheckoutPageListView(generic.ListView):
    template_name = 'checkout.html'

    def get(self, request):

        context = {
            'navbar': 'checkout',
        }

        return render(request, self.template_name, context)
    
    def post(self, request):

        form_address = BillingAddressForm(request.POST)

        if form_address.is_valid():
            form_address.save()
        else:
            form_address = BillingAddressForm()

        form_shipping = ShippingAddressForm(request.POST)

        if form_shipping.is_valid():
            form_shipping.save()
        else:
            form_shipping = ShippingAddressForm()

        context = {
            'navbar': 'checkout',
            'form_address': form_address,
            'form_shipping': form_shipping,
        }

        return render(request, self.template_name, context)
    

class ContactPageListView(generic.ListView):
    template_name = 'contact.html'

    def get(self, request):

        context = {
            'navbar': 'contact',
        }

        return render(request, self.template_name, context)
    
    def post(self, request):

        form = ContactUsForm(request.POST)

        if form.is_valid():
            form.save()
        else:
            form = ContactUsForm()

        context = {
            'navbar': 'contact',
            'form': form,
        }

        return render(request, self.template_name, context)


class ShopPageListView(generic.ListView):
    template_name = 'shop.html'

    def get(self, request):

        ourshop = OurShop.objects.get().product.all()
        for product in ourshop:
            product.discount_price = round(product.price * (1 - product.discount / 100), 2)

        context = {
            'navbar': 'shop',
            'ourshop': ourshop,
        }

        return render(request, self.template_name, context)
    

class ProductDetailView(generic.DetailView):
    template_name = 'detail.html'

    def get(self, request):

        context = {
            'navbar': 'detail',
        }

        return render(request, self.template_name, context)
    

















