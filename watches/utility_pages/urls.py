from django.urls import path

from .views import (about_page_view, confidential_page_view,
                    contacts_page_view, faq_page_view, terms_page_view)

app_name = 'utility_pages'

urlpatterns = [
    path('about', about_page_view, name='about'),
    path('contacts', contacts_page_view, name='contacts'),
    path('faq', faq_page_view, name='faq'),
    path('confidential', confidential_page_view, name='confidential'),
    path('terms', terms_page_view, name='terms'),
]
