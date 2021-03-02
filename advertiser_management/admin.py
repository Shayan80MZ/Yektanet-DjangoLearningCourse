from django.contrib import admin
from .models import Ad, Advertiser, View, Click


class AdAdmin(admin.ModelAdmin):
    list_display = ('title', 'approve',)
    list_filter = ('approve',)
    search_fields = ('title',)


admin.site.register(Ad, AdAdmin)
admin.site.register(Advertiser)
admin.site.register(View)
admin.site.register(Click)
