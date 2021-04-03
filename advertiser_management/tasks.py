from celery import task
from .models import Ad, HourlyData, DailyData
from datetime import datetime


@task(name='hourly_task')
def saveHourlyTask():
    for ad in Ad.objects.all():
        clickNum = ad.click_set.filter(click_date__gte=datetime.now().replace(hour=datetime.now().hour - 1, minute=0, second=0)).count()
        viewNum = ad.view_set.filter(view_date__gte=datetime.now().replace(hour=datetime.now().hour - 1, minute=0, second=0)).count()
        HourlyData.objects.create(ad=ad, clicksNum=clickNum, viewsNum=viewNum, date=datetime.now())


@task(name='daily_task')
def saveDailyTask():
    for ad in Ad.objects.all():
        clickNum = ad.click_set.filter(click_date__gte=datetime.now().replace(day=datetime.now().day - 1, minute=0, second=0)).count()
        viewNum = ad.view_set.filter(view_date__gte=datetime.now().replace(day=datetime.now().day - 1, minute=0, second=0)).count()
        DailyData.objects.create(ad=ad, clicksNum=clickNum, viewsNum=viewNum, date=datetime.now())
