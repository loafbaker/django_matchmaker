from django.urls import path

from . import views

app_name = 'matches'

urlpatterns = [
    path('position/<slug:slug>/', views.position_match_view,
        name='position_match_view'),
    path('location/<slug:slug>/', views.location_match_view,
        name='location_match_view'),
    path('employer/<slug:slug>/', views.employer_match_view,
        name='employer_match_view'),
]
