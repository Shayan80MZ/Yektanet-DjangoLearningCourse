from django.db import models


class Advertiser(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Ad(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField()
    link = models.URLField()
    advertiser = models.ForeignKey(Advertiser, on_delete=models.CASCADE)
    approve = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class View(models.Model):
    view_date = models.DateTimeField()
    user_ip = models.GenericIPAddressField()
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)


class Click(models.Model):
    click_date = models.DateTimeField()
    user_ip = models.GenericIPAddressField()
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)