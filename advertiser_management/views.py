from django.shortcuts import render, get_object_or_404
from django.views.generic import RedirectView, FormView
from .models import Ad, Advertiser, View, Click
from .forms import AdForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from datetime import datetime


def showAds(request):
    advertisers = Advertiser.objects.all()
    context = {"advertisers": advertisers}

    # increase ads views
    ads = Ad.objects.all()
    for ad in ads:
        view = View.objects.create(
            view_date=datetime.now(),
            user_ip=request.META['REMOTE_ADDR'],
            ad=ad
        )
        view.save()

    return render(request, 'advertiser_management/ads.html', context)


class CountClickAndRedirect(RedirectView):
    permanent = False
    query_string = True
    pattern_name = 'count-click'

    def get_redirect_url(self, *args, **kwargs):
        ad = get_object_or_404(Ad, pk=kwargs['pk'])
        click = Click.objects.create(
            click_date=datetime.now(),
            user_ip=self.request.META['REMOTE_ADDR'],
            ad=ad
        )
        click.save()
        self.url = ad.link
        return ad.link


class AdFormView(FormView):
    form_class = AdForm
    template_name = 'advertiser_management/form.html'

    def form_valid(self, form):
        advertiser_id = form.cleaned_data.get("advertiser_id")
        image = form.cleaned_data.get("image")
        title = form.cleaned_data.get("title")
        link = form.cleaned_data.get("link")
        ad = Ad.objects.create(
            title=title,
            image=image,
            link=link,
            advertiser=Advertiser.objects.get(pk=advertiser_id),
        )
        ad.save()
        return HttpResponseRedirect(reverse('show-ads'))
