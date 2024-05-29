from django.contrib import admin
from django.contrib.auth.models import Group, User

from .models import (
    Watch, Brand, Special, Shape, ForWho, Material,
    ConditionChoice, AvailabilityChoice
)

admin.site.unregister(Group)
admin.site.unregister(User)


@admin.register(Watch)
class WatchAdmin(admin.ModelAdmin):
    list_display = (
        'is_on_main', 'brand', 'title', 'availability', 'price', 'reference'
    )
    list_display_links = (
        'brand', 'title', 'availability', 'price', 'reference'
    )
    list_editable = (
        'is_on_main',
    )
    search_fields = (
        'title', 'brand__title', 'availability__title', 'material__title',
        'shape__title', 'for_who__title', 'special__title', 'condition__title',
        'reference', 'price'
    )
    list_filter = (
        'brand__title', 'availability__title', 'material__title',
        'shape__title', 'for_who__title', 'special__title', 'condition__title'
    )


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    pass


@admin.register(AvailabilityChoice)
class AvailabilityChoiceAdmin(admin.ModelAdmin):
    pass


@admin.register(ConditionChoice)
class ConditionChoiceAdmin(admin.ModelAdmin):
    pass


@admin.register(Special)
class SpecialAdmin(admin.ModelAdmin):
    pass


@admin.register(Shape)
class ShapeAdmin(admin.ModelAdmin):
    pass


@admin.register(ForWho)
class ForWhoAdmin(admin.ModelAdmin):
    pass


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    pass
