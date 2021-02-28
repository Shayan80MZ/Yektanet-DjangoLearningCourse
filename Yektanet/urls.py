from django.contrib import admin
from django.urls import path

from advertiser_management import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('show-ads/', views.showAds(), name='show-ads')
]
