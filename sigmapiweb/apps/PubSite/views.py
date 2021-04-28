"""
Views for PubSite app.
"""
from django.conf import settings
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.shortcuts import render
import requests

def _get_context(page_name):
    return {
        'pages': settings.PUBLIC_PAGES,
        'current_page_name': page_name,
    }

# Regular index
# def index(request):
#     """
#     View for the static index page
#     """
#     return render(request, 'public/home.html', _get_context('Home'))

# For having a campaign, renders copy of index.html 
def index(request):
    """
    View for the static index page
    """
    return render(request, 'public/home-campaign.html', _get_context('Home'))


def about(request):
    """
    View for the static chapter history page.
    """
    return render(request, 'public/about.html', _get_context('About'))


def activities(request):
    """
    View for the static chapter service page.
    """
    return render(
        request,
        'public/activities.html',
        _get_context('Service & Activities'),
    )

def rush(request):
    """
    View for the static chapter service page.
    """
    return render(
        request,
        'public/rush.html',
        _get_context('Rush'),
    )

def campaign(request):
    """
    View for the static chapter service page.
    """

    url = 'https://api.givebutter.com/v1/transactions/'
    headers = {'Authorization': f'Bearer {settings.GIVEBUTTER_API_KEY}'}
    response = None
    print(headers)
    # Make GET request to server, timeout in seconds
    try:
        r = requests.get(url, headers=headers, timeout=3, allow_redirects=False)
        if r.status_code == 301 or r.status_code == 307: # workaround for dropped auth headers due to redirect
            r = requests.get(r.headers['Location'], headers=headers, allow_redirects=False)
            if r.status_code == 301 or r.status_code == 307:  # workaround for dropped auth headers due to redirect
                r = requests.get(r.headers['Location'], headers=headers, allow_redirects=False)
                if r.status_code == 200:
                    response = r.json()
                else:
                    print(f"ERROR in re-request: {r.status_code}")
        else:
            print(f"ERROR in request: {r.status_code}")
    except requests.exceptions.Timeout:
        print("Connection Timed out")
    except requests.ConnectionError:
        print("Connection to GiveButter API could not be resolved")
    except requests.exceptions.RequestException:
        print("An unknown issue occurred while trying to retrieve GiveButter Donor List")

    # Check for successful response, if so - filter, sort, and format data
    if response and 'data' in response:
        print(f'Response: {response}')
        response = response['data']
        print(f'Data: {response}')
        successful_txs = [tx for tx in response if tx['status'] == 'success']
        print(f'Filtered: {successful_txs}')
        sorted_txs = sorted(successful_txs, key=lambda tx: tx['amount'], reverse=True)
        print(f'Sorted: {sorted_txs}')

    return render(
        request,
        'public/campaign.html',
        _get_context('Campaign'),
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