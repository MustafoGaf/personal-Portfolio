from django.shortcuts import render, get_object_or_404
from .models import Phone
def shop(req):
    phones = Phone.objects.all()
    return render(req, 'shop/shop.html', {"phones":phones})


def detail(req, shop_id):
    shop = get_object_or_404(Phone, pk=shop_id)
    return render(req, 'shop/detail.html', {"shop" : shop})
