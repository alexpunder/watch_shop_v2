from django.shortcuts import render


def index_page_view(request):
    return render(
        request,
        template_name='index.html'
    )


def buyback_view_page(request):
    return render(
        request,
        template_name='watches/buyback.html'
    )


def watches_page_view(request):
    return render(
        request,
        template_name='watches/watches.html'
    )


def watches_details_page_view(request):
    return render(
        request,
        template_name='watches/watches_details.html'
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
