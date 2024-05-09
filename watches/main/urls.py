from django.urls import path

from .views import index_page_view

app_name = 'main'

urlpatterns = [
    path('', index_page_view, name='index')
]
