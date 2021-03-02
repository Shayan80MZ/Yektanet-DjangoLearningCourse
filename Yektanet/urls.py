from django.contrib import admin
from django.urls import path

from advertiser_management import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('show-ads/', views.ShowAds.as_view(), name='show-ads'),
    path('click/<int:pk>/', views.CountClickAndRedirect.as_view(), name='count-click'),
    path('create-ad/', views.AdFormView.as_view(), name='create-ad'),
    path('ad-detail/<int:pk>/', views.AdDetail.as_view(), name='ad-detail')
]
