from django.urls import re_path

from . import views

app_name = 'matches'

urlpatterns = [
    re_path(r'^position/(?P<slug>[\w-]+)$', views.position_match_view,
        name='position_match_view'),
    re_path(r'^location/(?P<slug>[\w-]+)$', views.location_match_view,
        name='location_match_view'),
    re_path(r'^employer/(?P<slug>[\w-]+)$', views.employer_match_view,
        name='employer_match_view'),
]
