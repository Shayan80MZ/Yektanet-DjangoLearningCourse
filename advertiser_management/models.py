from django.db import models


class Advertiser(models.Model):
    advertiser_id = models.IntegerField()
    name = models.CharField(max_length=100)
    clicks = models.IntegerField(default=0)
    views = models.IntegerField(default=0)


class Ad(models.Model):
    ad_id = models.IntegerField()
    title = models.CharField(max_length=100)
    imgUrl = models.ImageField()
    link = models.URLField()
    clicks = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    advertiser = models.ForeignKey(Advertiser, on_delete=models.CASCADE)