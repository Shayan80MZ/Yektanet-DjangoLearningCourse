from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from advertiser_management import views

router = routers.DefaultRouter()

router.register(r'register-advertiser', views.RegisterAdvertiserView, basename='register-advertiser')
router.register(r'create-ad', views.CreateAdView, basename='create-ad')
router.register(r'edit-ad', views.EditAdView, basename='edit-ad')
router.register(r'ad-clicks', views.AdClicksView, basename='ad-clicks')
router.register(r'ad-views', views.AdViewsView, basename='ad-views')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
