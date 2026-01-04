"""
URL configuration for django_matchmaker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path

from dashboard import views as dashboard_views
from likes import views as likes_views
from newsletter import views as newsletter_views
from profiles import views as profiles_views
from questions import views as questions_views

from . import views as django_matchmaker_views

urlpatterns = [
    path('', dashboard_views.home, name='home'),
    path('question/', questions_views.home, name='question_home'),
    re_path(r'^question/(?P<id>\d+)$', questions_views.single, name='question_single'),
    path('contact/', newsletter_views.contact, name='contact'),
    path('about/', django_matchmaker_views.about, name='about'),
    re_path(r'^like/(?P<id>\d+)$', likes_views.like_user, name='like_user'),
    path('profile/edit/', profiles_views.profile_edit, name='profile_edit'),
    re_path(r'^profile/(?P<username>[\w.@+-]+)$', profiles_views.profile_view, name='profile'),
    path('profile/jobs/add/', profiles_views.job_add, name='job_add'),
    path('profile/jobs/edit/', profiles_views.jobs_edit, name='jobs_edit'),
    path('profile/', profiles_views.profile_user, name='profile_user'),
    # path('blog/', include('blog.urls')),

    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.default.urls')),
    path('matches/', include('matches.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
