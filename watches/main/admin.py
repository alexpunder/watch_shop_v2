from django.contrib import admin

from .models import (
    Watch, Brand, Special, Shape, ForWho, Material,
    ConditionChoice, AvailabilityChoice
)


@admin.register(Watch)
class WatchAdmin(admin.ModelAdmin):
    pass


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
