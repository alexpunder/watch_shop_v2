from django.contrib import admin

from .models import (
    ShortMain, BuybackWatches, BuybackImage,
    ValuationWatches, ValuationImage, WatchRequest
)


class BuybackImagesInline(admin.TabularInline):
    model = BuybackImage
    extra = 0


class ValuationImagesInline(admin.TabularInline):
    model = ValuationImage
    extra = 0


@admin.register(ValuationWatches)
class ValuationWatchesAdmin(admin.ModelAdmin):
    inlines = [ValuationImagesInline]


@admin.register(BuybackWatches)
class BuybackWatchAdmin(admin.ModelAdmin):
    inlines = [BuybackImagesInline]


@admin.register(ShortMain)
class ShortMainAdmin(admin.ModelAdmin):
    pass


@admin.register(WatchRequest)
class WatchRequestAdmin(admin.ModelAdmin):
    pass
