from django import forms


class AdForm(forms.Form):
    advertiser_id = forms.IntegerField()
    image = forms.ImageField()
    title = forms.CharField()
    link = forms.URLField()