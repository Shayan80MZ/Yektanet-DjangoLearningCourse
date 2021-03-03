from django.shortcuts import render, get_object_or_404
from django.views.generic import RedirectView, FormView, base, DetailView
from .models import Ad, Advertiser, View, Click
from .forms import AdForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from datetime import datetime

from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework import generics, viewsets, status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView
from rest_framework.mixins import *
from .serializers import *
from .permissions import *


class RegisterAdvertiserView(viewsets.GenericViewSet, CreateModelMixin):
    serializer_class = AdvertiserSerializer
    queryset = Advertiser.objects.all()

    def create(self, request, *args, **kwargs):
        name = request.data.get("name")
        user = User.objects.create(username=name)
        token = Token.objects.create(user=user).key
        advertiser = Advertiser(name=name, user=user)
        advertiser.save()

        return Response({'token': token}, status=status.HTTP_200_OK)


class CreateAdView(viewsets.GenericViewSet, CreateModelMixin):
    serializer_class = AdSerializer
    queryset = Ad.objects.all()
    authentication_classes =[TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]


class EditAdView(viewsets.GenericViewSet, RetrieveModelMixin):
    serializer_class = AdSerializer
    queryset = Ad.objects.all()
    authentication_classes =[TokenAuthentication, ]
    permission_classes = [IsAuthenticated, IsAdAdvertiser]


class AdClicksView(viewsets.GenericViewSet, ListModelMixin):
    serializer_class = ClickSerializer
    queryset = Click.objects.all()
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, IsAdAdvertiser]

    def get_queryset(self):
        return Click.objects.filter(ad__advertiser__name=self.request.user.username)


class AdViewsView(viewsets.GenericViewSet, ListModelMixin):
    serializer_class = ViewSerializer
    queryset = View.objects.all()
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, IsAdAdvertiser]

    def get_queryset(self):
        return View.objects.filter(ad__advertiser__name=self.request.user.username)