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

    ex_data = [{
    "id": "OR2Q93LZhKm1PL66",
    "campaign_id": 71,
    "team_id": None,
    "member_id": None,
    "first_name": "John",
    "last_name": "Doe",
    "email": "johndoe@example.net",
    "phone": "(271) 555-1212",
    "address": {
        "address_1": "4 Privet Drive",
        "address_2": None,
        "city": "Newark",
        "state": "NJ",
        "zipcode": "07104",
        "country": "USA"
    },
    "status": "succeeded",
    "method": "card",
    "amount": 49,
    "fee": 3.29,
    "fee_covered": 3.29,
    "donated": 49,
    "payout": 49,
    "currency": "USD",
    "created_at": "2020-05-15 19:50:02",
    "giving_space": {
        "id": 263,
        "name": "John Doe",
        "amount": 49,
        "message": None
    },
    "transactions": [
        {
            "id": "7535510393",
            "plan_id": None,
            "amount": 49,
            "fee": 3.29,
            "fee_covered": 3.29,
            "donated": 49,
            "payout": 49,
            "captured": True,
            "captured_at": "2020-05-15 19:50:03",
            "refunded": False,
            "line_items": [
                {
                    "type": "item",
                    "subtype": "ticket",
                    "description": "General Admission",
                    "quantity": 1,
                    "price": 49,
                    "discount": 0,
                    "total": 49
                },
                {
                    "type": "donation",
                    "subtype": "fee",
                    "description": "Processing fee",
                    "quantity": 1,
                    "price": 3.29,
                    "discount": 0,
                    "total": 3.29
                }
            ]
        }
    ]
}]

    url = 'https://api.givebutter.com/v1/transactions/'
    headers = {'Authorization': f'Bearer {settings.GIVEBUTTER_API_KEY}'}
    response = None
    print(headers)
    # Make GET request to server, timeout in seconds
    try:
        r = requests.get(url, headers=headers, timeout=1, allow_redirects=False)
        if r.status_code == 301 or r.status_code == 307: # workaround for dropped auth headers due to redirect
            r = requests.get(r.headers['Location'], timeout=1, headers=headers, allow_redirects=False)
            if r.status_code == 301 or r.status_code == 307:  # workaround for dropped auth headers due to redirect
                r = requests.get(r.headers['Location'], timeout=1, headers=headers, allow_redirects=False)
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

    ctx = _get_context('Campaign')

    # Check for successful response, if so - filter, sort, and format data
    if response and 'data' in response:
        print(f'Response: {response}')
        response = ex_data # response['data']
        print(f'Data: {response}')
        successful_txs = [tx for tx in response if tx['status'] == 'succeeded']
        print(f'Filtered: {successful_txs}')
        sorted_txs = sorted(successful_txs, key=lambda tx: tx['amount'], reverse=True)
        print(f'Sorted: {sorted_txs}')
        transactions = [{'first_name': tx['first_name'], 'last_name': tx['last_name'], 'amount': tx['amount'], 'message': tx['giving_space']['message']} for tx in sorted_txs]
        print(f'Transactions: {transactions}')
        ctx['transactions'] = transactions

    return render(
        request,
        'public/campaign.html',
        ctx,
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