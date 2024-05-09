from django.urls import path

from .views import (
    index_page_view, about_page_view, contacts_page_view, faq_page_view
)

app_name = 'main'

urlpatterns = [
    path('', index_page_view, name='index'),
    path('about', about_page_view, name='about'),
    path('contacts', contacts_page_view, name='contacts'),
    path('faq', faq_page_view, name='faq'),
]
