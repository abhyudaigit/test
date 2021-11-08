from django.conf.urls import url
from django.urls.conf import path
from . import views

urlpatterns = [
    path("",views.index, name="ShopHome"),
    path("about/",views.about, name="AboutUs"),
    path("contact/",views.contact, name="ContactUs"),
    path("tracker/",views.tracker, name="TrackingStatus"),
    path("search/",views.search, name="Search"),
    path("productview",views.productview, name="ViewOurProduct"),
    path("checkout/",views.checkout, name="Checkout"),
]