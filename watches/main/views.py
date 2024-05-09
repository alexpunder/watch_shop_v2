from django.shortcuts import render


def index_page_view(request):
    return render(
        request,
        template_name='index.html'
    )
