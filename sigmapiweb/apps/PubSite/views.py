"""
Views for PubSite app.
"""
from django.http import JsonResponse
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.shortcuts import render
from .forms import ContactForm
from django.views.decorators.http import require_POST
from common.utils import send_email
from common.settings.base import EC_EMAIL


def _get_context(page_name):
    return {
        'pages': settings.PUBLIC_PAGES,
        'current_page_name': page_name,
    }


def index(request):
    """
    View for the static index page
    """
    return render(request, 'public/home.html', _get_context('Home'))


def about(request):
    """
    View for the static chapter history page.
    """
    return render(request, 'public/about.html', _get_context('About'))


def contact(request):
    """
    View for the contact us page.
    """
    context = _get_context('Contact')
    contact_form = None

    if request.method == 'POST':
        contact_form = _send_contact_form(request)
    else:
        contact_form = ContactForm()

    context.update({
        'contact_us_form': contact_form
    })

    return render(request, 'public/contact.html', context)


def _send_contact_form(request):
    """
    Helper for submitting the contact form and sending the email
    """
    form = ContactForm(request.POST)
    if form.is_valid():
        sender = form.cleaned_data.get('sender')
        body = form.cleaned_data.get('message')
        response_email = form.cleaned_data.get('response_email')
        subject = 'Email from {sender} via Contact Us page on the website'.format(sender=sender)
        body = '''
        A contact request was sent by {sender} via the website. The body of the email is as follows:
        -------
        {body}
        -------
        The sender left the following email for reply: {response_email}
        
        Please contact the Web chair if you experience any technical difficulties with this email.
        '''.format(sender=sender, body=body, response_email=response_email)
        to_emails = [EC_EMAIL]
        cc_emails = []
        send_email(subject, body, to_emails, cc_emails)
        messages.success(request, 'Success!')
    else:
        message = 'Failed to send message.'
        messages.error(request, message)
    return form


def activities(request):
    """
    View for the static chapter service page.
    """
    return render(
        request,
        'public/activities.html',
        _get_context('Service & Activities'),
    )


def permission_denied(request):
    """
    View for 403 (Permission Denied) error.
    """
    return render(
        request, 'common/403.html', _get_context('Permission Denied'),
    )


def handler404(request, exception):
    """

    """
    return render(request, 'common/404.html', _get_context("Page Not Found"))


class ResetPassword(PasswordResetView):
    template_name = "password_reset/password_reset_form.html"


class ResetPasswordDone(PasswordResetDoneView):
    template_name = "password_reset/password_reset_done.html"


class ResetPasswordConfirm(PasswordResetConfirmView):
    template_name = "password_reset/password_reset_confirm.html"

class ResetPasswordComplete(PasswordResetCompleteView):
    template_name = "password_reset/password_reset_complete.html"