from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Watch

EXCLUDE_FIELDS = (
    'id', 'title', 'is_on_main', 'condition', 'availability', 'special',
    'for_who', 'shape', 'price', 'reference', 'image'
)


def index_page_view(request):
    watches = Watch.objects.filter(
        is_on_main=True
    )
    return render(
        request,
        template_name='index.html',
        context={'watches': watches}
    )


def buyback_view_page(request):
    return render(
        request,
        template_name='watches/buyback.html'
    )


def watches_page_view(request):
    watches = Watch.objects.all()
    return render(
        request,
        template_name='watches/watches.html',
        context={'watches': watches}
    )


def watches_details_page_view(request, watch_id):
    watch = get_object_or_404(Watch, id=watch_id)
    data = {}

    for field in watch._meta.fields:
        if field.name not in EXCLUDE_FIELDS:
            verbose_name = field.verbose_name
            field_name = field.name
            value = getattr(watch, field_name)
            data[verbose_name] = value

    return render(
        request,
        template_name='watches/watches_details.html',
        context={'watch': watch, 'data': data.items()}
    )


def watches_valuation_page_view(request):
    return render(
        request,
        template_name='watches/valuation.html'
    )


def about_page_view(request):
    return render(
        request,
        template_name='pages/about.html'
    )


def contacts_page_view(request):
    return render(
        request,
        template_name='pages/contacts.html'
    )


def faq_page_view(request):
    return render(
        request,
        template_name='pages/faq.html'
    )


def confidential_page_view(request):
    return render(
        request,
        template_name='pages/confidential.html'
    )


def terms_page_view(request):
    return render(
        request,
        template_name='pages/terms.html'
    )


def page_not_found(request, exception):
    return render(request, 'pages/404.html', status=404)


def server_error(request):
    return render(
        request, 'pages/500.html', status=500)
