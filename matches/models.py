from django.db import models
from django.conf import settings

# Create your models here.
from .utils import get_match

class MatchManager(models.Manager):
    def get_or_create_match(self, user_a=None, user_b=None):
        try:
            obj = self.get(user_a=user_a, user_b=user_b)
        except:
            obj = None

        try:
            obj_2 = self.get(user_a=user_b, user_b=user_a)
        except:
            obj_2 = None

        if obj:
            return obj, False
        elif obj_2:
            return obj_2, False
        else:
            new_instance = self.create(user_a=user_a, user_b=user_b)
            match_decimal, question_answered = get_match(user_a, user_b)
            new_instance.match_decimal = match_decimal
            new_instance.questions_answered = question_answered
            new_instance.save()
            return new_instance, True


class Match(models.Model):
    user_a = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='match_user_a')
    user_b = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='match_user_b')
    match_decimal = models.DecimalField(default=0.00, decimal_places=8, max_digits=16)
    questions_answered = models.IntegerField(default=0)
    # is good match?
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    objects = MatchManager()

    def __unicode__(self):
        return '%.2f' % (self.match_decimal)

    def do_match(self):
        user_a = self.user_a
        user_b = self.user_b
        match_decimal, question_answered = get_match(user_a, user_b)
        self.match_decimal = match_decimal
        self.questions_answered = question_answered
        self.save()


