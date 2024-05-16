from django.urls import path

from .views import (
    index_page_view, watches_valuation_page_view, watches_page_view,
    watches_details_page_view, buyback_view_page
)

app_name = 'main'

urlpatterns = [
    path('', index_page_view, name='index'),
    path('buyback', buyback_view_page, name='buyback'),
    path('watches', watches_page_view, name='watches'),
    path(
        'watches-details/<int:watch_id>/',
        watches_details_page_view,
        name='watches_details'
    ),
    path('watches-valuation', watches_valuation_page_view, name='valuation'),
]
