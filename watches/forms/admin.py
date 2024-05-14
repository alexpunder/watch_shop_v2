from django.contrib import admin

from .models import ShortMain, BuybackWatch


@admin.register(ShortMain)
class ShortMainAdmin(admin.ModelAdmin):
    pass


@admin.register(BuybackWatch)
class BuybackWatchAdmin(admin.ModelAdmin):
    pass
