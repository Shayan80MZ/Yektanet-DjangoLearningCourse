from celery import task


@task(name='hourly_task')
def saveHourlyTask():
    pass


@task(name='daily_task')
def saveDailyTask():
    pass
