from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import Http404

# Create your views here.
from .models import Profile

from matches.models import Match

User = get_user_model()

@login_required
def profile_view(request, username):
    user = get_object_or_404(User, username=username)
    profile, created = Profile.objects.get_or_create(user=user)
    match, match_created = Match.objects.get_or_create_match(user_a=request.user, user_b=user)
    context = {
        'profile': profile,
        'match': match,
     }
    return render(request, 'profiles/profile_view.html', context)
