from django.conf.urls import url
from views import main, verification

urlpatterns = [
    url(r'^main/$', main, name='main'),
    url(r'^$', verification, name='verification')
]
