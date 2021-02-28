from django.shortcuts import render
from .models import Ad, Advertiser


def showAds(request):
    advertisers = Advertiser.objects.all()
    context = {"advertisers_list": advertisers}

    # increase ads views
    ads = Ad.objects.all()
    for ad in ads:
        ad.views += 1

    return render(request, 'advertiser_management/ads.html', context)


def countClicks():
    pass


def createAd():
    pass
