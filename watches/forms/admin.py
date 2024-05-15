from django.contrib import admin

from .models import ShortMain, BuybackWatch, BuybackImage


class ImagesInline(admin.TabularInline):
    model = BuybackImage
    extra = 0


@admin.register(ShortMain)
class ShortMainAdmin(admin.ModelAdmin):
    pass


@admin.register(BuybackWatch)
class BuybackWatchAdmin(admin.ModelAdmin):
    inlines = [ImagesInline]
