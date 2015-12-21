from django.db import models
from django.conf import settings

# Create your models here.

User = settings.AUTH_USER_MODEL

class UserLikeManager(models.Manager):
	def get_all_mutual_likes(self, user):
		qs = user.liker.liked_users.all().order_by('?')
		mutual_users = []
		for other_user in qs:
			try:
				if other_user.liker.get_mutual_like(user):
					mutual_users.append(other_user)
			except:
				pass
		return mutual_users


class UserLike(models.Model):
	user = models.OneToOneField(User, related_name='liker')
	liked_users = models.ManyToManyField(User, related_name='liked_users', blank=True)

	objects = UserLikeManager()

	def __unicode__(self):
		return self.user.username

	def get_mutual_like(self, user_b):
		i_like = False
		u_like = False
		if user_b in self.liked_users.all():
			i_like = True

		liked_user, created = UserLike.objects.get_or_create(user=user_b)
		if self.user in liked_user.liked_users.all():
			u_like = True

		return i_like and u_like

