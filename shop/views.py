from django.shortcuts import render
from django.http import HttpResponse
from.models import Product
from math import ceil

# Create your views here.
def index(request):
    allProds=[]
    catprods= Product.objects.values('category', 'id')
    cats= {item["category"] for item in catprods}
    for cat in cats:
        prod=Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    params={'allProds':allProds }
    return render(request,"shop/index.html", params)

def about(request):
    allProds=[]
    catprods= Product.objects.values('category', 'id')
    cats= {item["category"] for item in catprods}
    for cat in cats:
        prod=Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    params={'allProds':allProds }
    return render(request,"shop/about.html", params)
   
    
def contact(request):
    return HttpResponse("CONTACT FOR ANY QUERIES")

def tracker(request):
    return HttpResponse("TRACK YOUR ORDER")

def search(request):
    return HttpResponse("SEARCH PRODUCT")

def productview(request):
    return HttpResponse("SEE YOUR PRODUCT HERE")

def checkout(request):
    return HttpResponse(" CLICK TO CHECKOUT")