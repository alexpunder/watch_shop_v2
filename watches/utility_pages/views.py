from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages

from forms.forms import FeedbackForm
from main.tasks import send_message
from watches.constants import DT_FORMAT, TITLES_DATA, DESCRIPTIONS_DATA


def about_page_view(request):
    return render(
        request,
        template_name='utility_pages/about.html',
        context={
            'title': TITLES_DATA.get('about'),
            'description': DESCRIPTIONS_DATA.get('about')
        }
    )


def contacts_page_view(request):
    form = FeedbackForm()

    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            data = form.save()
            send_message(
                'КОНТАКТНАЯ ФОРМА',
                data.pub_date.strftime(DT_FORMAT), data.id
            )

            messages.success(
                request,
                message=(
                    'Ваше сообщение успешно отправлено. '
                    'Благодарим за обратную связь!'
                )
            )
            return HttpResponseRedirect(
                request.META.get('HTTP_REFERER')
            )
        else:
            messages.warning(
                request,
                message=(
                    'Ошибка заполнения формы: '
                    f'{form.errors.as_text()}'
                )
            )

    return render(
        request,
        template_name='utility_pages/contacts.html',
        context={
            'form': form,
            'title': TITLES_DATA.get('contacts'),
            'description': DESCRIPTIONS_DATA.get('contacts')
        }
    )


def faq_page_view(request):
    return render(
        request,
        template_name='utility_pages/faq.html',
        context={
            'title': TITLES_DATA.get('faq'),
            'description': DESCRIPTIONS_DATA.get('faq')
        }
    )


def confidential_page_view(request):
    return render(
        request,
        template_name='utility_pages/confidential.html',
        context={
            'title': TITLES_DATA.get('confidential'),
            'description': DESCRIPTIONS_DATA.get('confidential')
        }
    )


def terms_page_view(request):
    return render(
        request,
        template_name='utility_pages/terms.html',
        context={
            'title': TITLES_DATA.get('terms'),
            'description': DESCRIPTIONS_DATA.get('terms')
        }
    )


def page_not_found(request, exception):
    return render(
        request,
        'utility_pages/404.html',
        context={
            'title': TITLES_DATA.get('terms'),
            'description': DESCRIPTIONS_DATA.get('terms')
        },
        status=404
    )


def server_error(request):
    return render(
        request,
        'utility_pages/500.html',
        status=500
    )
