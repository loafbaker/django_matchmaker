from django.contrib.auth import get_user_model
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.dispatch import Signal

from .models import Match, PositionMatch


User = get_user_model()

@receiver(user_logged_in)
def get_user_matches_receiver(sender, request, user, *args, **kwargs):
	for u in User.objects.exclude(username=user.username).order_by('-id')[:200]:
		Match.objects.get_or_create_match(user_a=u, user_b=user)


user_matches_update = Signal(providing_args=['user'])

def user_matches_update_receiver(sender, user, *args, **kwargs):
	updated = Match.objects.update_for_user(user)
	update_top_suggestions = PositionMatch.objects.update_top_suggestions(user, 20)

user_matches_update.connect(user_matches_update_receiver)