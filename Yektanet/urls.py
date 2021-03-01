from django.contrib import admin
from django.urls import path

from advertiser_management import views
#
# app_name = "advertiser_management"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('show-ads/', views.showAds, name='show-ads'),
    path('<int:pk>/', views.CountClickAndRedirect.as_view(), name='count-click'),
    path('create-ad/', views.AdFormView.as_view(), name='create-ad')
]
