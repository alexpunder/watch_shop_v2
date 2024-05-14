from django.urls import path

from .views import (
    footer_form_view, index_page_short_form, feedback_form_view,
    call_form_view, watch_request_form_view
)

app_name = 'forms'

urlpatterns = [
    path('footer-form', footer_form_view, name='footer_form'),
    path('short-index-form', index_page_short_form, name='short_index'),
    path('feedback-contact-form', feedback_form_view, name='feedback_form'),
    path('call-form', call_form_view, name='call_form'),
    path('watch-request-form', watch_request_form_view, name='watch_request')
]
