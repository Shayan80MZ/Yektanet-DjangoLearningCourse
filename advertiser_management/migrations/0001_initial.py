# Generated by Django 3.1.6 on 2021-03-01 22:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='')),
                ('link', models.URLField()),
                ('clicks', models.IntegerField(default=0)),
                ('views', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Advertiser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('clicks', models.IntegerField(default=0)),
                ('views', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='View',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('view_date', models.DateTimeField()),
                ('user_ip', models.GenericIPAddressField()),
                ('ad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='advertiser_management.ad')),
            ],
        ),
        migrations.CreateModel(
            name='Click',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('click_date', models.DateTimeField()),
                ('user_ip', models.GenericIPAddressField()),
                ('ad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='advertiser_management.ad')),
            ],
        ),
        migrations.AddField(
            model_name='ad',
            name='advertiser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='advertiser_management.advertiser'),
        ),
    ]
