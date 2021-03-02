from django.db import models
from collections import OrderedDict


class Advertiser(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def getApprovedAds(self):
        for ad in self.ad_set.all():
            if ad.approve:
                yield ad


class Ad(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField()
    link = models.URLField()
    advertiser = models.ForeignKey(Advertiser, on_delete=models.CASCADE)
    approve = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def getClicksNumber(self):
        dict = {}
        for hour in range(0, 24):
            dict[str(hour) + "-" + str(hour+1)] = self.click_set.filter(ad__click__click_date__hour__range=(hour, hour+1)).count()

        return dict

    def getViewsNumber(self):
        dict = {}
        for hour in range(0, 24):
            dict[str(hour) + "-" + str(hour + 1)] = self.view_set.filter(ad__view__view_date__hour__range=(hour, hour+1)).count()

        return dict

    def getClickRateToView(self):
        dict = {}
        for hour in range(0, 24):
            if self.click_set.filter(ad__click__click_date__hour__range=(hour, hour+1)).exists():
                dict[str(hour) + "-" + str(hour + 1)] = self.click_set.filter(ad__click__click_date__hour__range=(hour, hour+1)).count() / self.view_set.filter(ad__view__view_date__hour__range=(hour, hour+1)).count()

        return OrderedDict(sorted(dict.items(), key=lambda x: x[1], reverse=True))

    def getAveViewAndClickTimeDif(self):
        sum = 0
        for click in self.click_set.all():
            time = click.click_date - self.view_set.filter(user_ip=click.user_ip).filter(view_date__lt=click.click_date)[0].view_date
            sum += time.seconds

        if self.click_set.exists():
            return sum / self.click_set.count()
        else:
            return "we have no clicks on this ad"


class View(models.Model):
    view_date = models.DateTimeField()
    user_ip = models.GenericIPAddressField()
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)

    def __str__(self):
        return self.ad.title + " viewed by " + self.user_ip


class Click(models.Model):
    click_date = models.DateTimeField()
    user_ip = models.GenericIPAddressField()
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)

    def __str__(self):
        return self.ad.title + " clicked by " + self.user_ip
