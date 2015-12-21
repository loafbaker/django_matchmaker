from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

# Create your views here.
from .models import UserLike

User = get_user_model()

@login_required
def like_user(request, id):
	pending_like = get_object_or_404(User, id=id)
	user_like, created = UserLike.objects.get_or_create(user=request.user)
	if pending_like in user_like.liked_users.all():
		user_like.liked_users.remove(pending_like)
	else:
		user_like.liked_users.add(pending_like)

	return redirect('profile', username=pending_like.username)