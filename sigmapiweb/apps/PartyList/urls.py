"""
URLs for PartyList app.
"""
from django.conf.urls import url
from django.views.generic import RedirectView

from . import views, api


urlpatterns = [
    url(
        regex=r"^$",
        view=RedirectView.as_view(pattern_name="partylist-old-index"),
        name="partylist-old-index",
    ),
    url(
        regex=r"^all/$",
        view=views.index,
        name="partylist-old-index",
    ),
    url(
        regex=r"^add/$",
        view=views.add_party,
        name="partylist-old-add_party",
    ),
    url(
        regex=r"^manage/$",
        view=views.manage_parties,
        name="partylist-old-manage_parties",
    ),
    url(
        regex=r"^edit/(?P<party_id>[\d]+)/$",
        view=views.edit_party,
        name="partylist-old-edit_party",
    ),
    url(
        regex=r"^refresh/(?P<party_id>[\d]+)/$",
        view=views.refresh_party_listings,
        name="partylist-old-refresh_party_listings",
    ),
    url(
        regex=r"^delete/(?P<party_id>[\d]+)/$",
        view=views.delete_party,
        name="partylist-old-delete_party",
    ),
    url(
        regex=r"^view/(?P<party_id>[\d]+)/guests/$",
        view=views.guests,
        name="partylist-old-guests",
    ),
    url(
        regex=r"^view/(?P<party_id>[\d]+)/guests/create/$",
        view=api.create,
        name="partylist-old-api-create",
    ),
    url(
        regex=(
            r"^view/(?P<party_id>[\d]+)/guests/destroy/" r"(?P<party_guest_id>[\d]+)/$"
        ),
        view=api.destroy,
        name="partlist-api-destroy",
    ),
    url(
        regex=(
            r"^view/(?P<party_id>[\d]+)/guests/signIn/" r"(?P<party_guest_id>[\d]+)/$"
        ),
        view=api.sign_in,
        name="partylist-old-api-signin",
    ),
    url(
        regex=(
            r"^view/(?P<party_id>[\d]+)/guests/signOut/" r"(?P<party_guest_id>[\d]+)/$"
        ),
        view=api.sign_out,
        name="partylist-old-api-signout",
    ),
    url(
        regex=r"^view/(?P<party_id>[\d]+)/guests/poll/$",
        view=api.poll,
        name="partylist-old-api-poll",
    ),
    url(
        regex=r"^view/(?P<party_id>[\d]+)/guests/export/$",
        view=api.export_list,
        name="partylist-old-api-export_list",
    ),
    url(
        regex=r"^view/(?P<party_id>[\d]+)/guests/count/delta/$",
        view=api.update_manual_delta,
        name="partylist-old-api-updateManualDelta",
    ),
    url(
        regex=r"^view/(?P<party_id>[\d]+)/guests/count/poll/$",
        view=api.poll_count,
        name="partylist-old-api-pollCount",
    ),
    url(
        regex=r"^view/(?P<party_id>[\d]+)/guests/init/$",
        view=api.init_pulse,
        name="partylist-old-api-initPulse",
    ),
]
