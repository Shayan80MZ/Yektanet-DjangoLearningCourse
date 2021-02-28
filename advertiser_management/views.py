from django.shortcuts import render, get_object_or_404
from django.views.generic import RedirectView
from .models import Ad, Advertiser


def showAds(request):
    advertisers = Advertiser.objects.all()
    context = {"advertisers_list": advertisers}

    # increase ads views
    ads = Ad.objects.all()
    for ad in ads:
        ad.views += 1
        ad.save()

    return render(request, 'advertiser_management/ads.html', context)


class CountClickAndRedirect(RedirectView):
    permanent = False
    query_string = True
    pattern_name = 'count-click'

    def get_redirect_url(self, *args, **kwargs):
        ad = get_object_or_404(Ad, pk=kwargs['pk'])
        ad.clicks += 1
        ad.save()
        self.url = ad.link
        return ad.link


def createAd():
    pass
