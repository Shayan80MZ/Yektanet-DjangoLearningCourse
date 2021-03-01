from django.db import models


class Advertiser(models.Model):
    name = models.CharField(max_length=100)
    clicks = models.IntegerField(default=0)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Ad(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField()
    link = models.URLField()
    clicks = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    advertiser = models.ForeignKey(Advertiser, on_delete=models.CASCADE)

    def __str__(self):
        return self.title