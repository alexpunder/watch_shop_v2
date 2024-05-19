from django.contrib import admin

from .models import (
    ShortMain, BuybackWatches, BuybackImage, Call,
    ValuationWatches, ValuationImage, WatchRequest,
    Feedback
)


class BuybackImagesInline(admin.TabularInline):
    model = BuybackImage
    extra = 0

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


class ValuationImagesInline(admin.TabularInline):
    model = ValuationImage
    extra = 0

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(ValuationWatches)
class ValuationWatchesAdmin(admin.ModelAdmin):
    inlines = [ValuationImagesInline]
    list_display = (
        'processed', 'name', 'phone', 'email', 'communication_method',
        'pub_date'
    )
    list_display_links = (
        'name', 'phone', 'email', 'pub_date'
    )
    list_editable = (
        'processed',
    )
    search_fields = (
        'name', 'phone', 'email', 'pub_date'
    )
    list_filter = (
        'processed',
    )
    readonly_fields = (
        'name', 'phone', 'text', 'email', 'communication_method',
        'brand', 'model', 'year', 'price', 'condition', 'equipment',
        'pub_date'
    )


@admin.register(BuybackWatches)
class BuybackWatchAdmin(admin.ModelAdmin):
    inlines = [BuybackImagesInline]
    list_display = (
        'processed', 'name', 'phone', 'email', 'communication_method',
        'pub_date'
    )
    list_display_links = (
        'name', 'phone', 'email', 'pub_date'
    )
    list_editable = (
        'processed',
    )
    search_fields = (
        'name', 'phone', 'email', 'pub_date'
    )
    list_filter = (
        'processed',
    )
    readonly_fields = (
        'name', 'phone', 'text', 'email', 'communication_method',
        'brand', 'model', 'year', 'price', 'condition', 'equipment',
        'pub_date',
    )


@admin.register(ShortMain)
class ShortMainAdmin(admin.ModelAdmin):
    list_display = (
        'processed', 'name', 'phone', 'text', 'pub_date'
    )
    list_display_links = (
        'name', 'phone', 'text', 'pub_date'
    )
    list_editable = (
        'processed',
    )
    search_fields = (
        'name', 'phone', 'pub_date'
    )
    list_filter = (
        'processed',
    )
    readonly_fields = (
        'name', 'phone', 'text', 'pub_date'
    )


@admin.register(WatchRequest)
class WatchRequestAdmin(admin.ModelAdmin):
    list_display = (
        'processed', 'name', 'phone', 'hiden_info', 'pub_date'
    )
    list_display_links = (
        'name', 'phone', 'hiden_info', 'pub_date'
    )
    list_editable = (
        'processed',
    )
    search_fields = (
        'name', 'phone', 'hiden_info', 'pub_date'
    )
    list_filter = (
        'processed',
    )
    readonly_fields = (
        'name', 'phone', 'hiden_info', 'pub_date'
    )


@admin.register(Call)
class CallAdmin(admin.ModelAdmin):
    list_display = (
        'processed', 'name', 'phone', 'pub_date'
    )
    list_display_links = (
        'name', 'phone', 'pub_date'
    )
    list_editable = (
        'processed',
    )
    search_fields = (
        'name', 'phone', 'pub_date'
    )
    list_filter = (
        'processed',
    )
    exclude = ('text',)
    readonly_fields = ('name', 'phone')


@admin.register(Feedback)
class WatchRequestAdmin(admin.ModelAdmin):
    list_display = (
        'processed', 'name', 'phone', 'pub_date'
    )
    list_display_links = (
        'name', 'phone', 'pub_date'
    )
    list_editable = (
        'processed',
    )
    search_fields = (
        'name', 'phone', 'pub_date'
    )
    list_filter = (
        'processed',
    )
    readonly_fields = (
        'name', 'phone', 'pub_date'
    )
