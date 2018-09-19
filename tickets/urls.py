from django.conf.urls import url, include
from .views import all_tickets, one_ticket, create_ticket


urlpatterns = [
    url(r'^$', all_tickets, name='tickets'),
    url(r'^(?P<ticket_id>\d+)/$', one_ticket, name='ticket'),
    url(r'^create/$', create_ticket, name='create_ticket'),
]