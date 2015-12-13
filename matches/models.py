import datetime
from django.utils import timezone
from django.db import models
from django.conf import settings

# Create your models here.
from .utils import get_match
class MatchQuerySet(models.query.QuerySet):
    def all(self):
        return self.filter(active=True)

    def matches(self, user):
        q1 = self.filter(user_a=user)
        q2 = self.filter(user_b=user)
        return (q1 | q2).distinct()


class MatchManager(models.Manager):
    def get_queryset(self):
        return MatchQuerySet(self.model, using=self._db)

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
            obj.check_update()
            return obj, False
        elif obj_2:
            obj_2.check_update()
            return obj_2, False
        else:
            new_instance = self.create(user_a=user_a, user_b=user_b)
            new_instance.do_match()
            return new_instance, True

    def update_all(self):
        queryset = self.all()
        now = timezone.now()
        offset = now - datetime.timedelta(hours=12)
        offset2 = now - datetime.timedelta(hours=36) 
        queryset.filter(updated__gt=offset2).filter(updated__lte=offset)
        if queryset.count > 0:
            for i in queryset:
                i.check_update()

    def matches_all(self, user):
        return self.get_queryset().matches(user)

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

    @property
    def get_percent(self):
        return '%.2f%%' % (self.match_decimal * 100)

    def do_match(self):
        user_a = self.user_a
        user_b = self.user_b
        match_decimal, question_answered = get_match(user_a, user_b)
        self.match_decimal = match_decimal
        self.questions_answered = question_answered
        self.save()

    def check_update(self):
        now = timezone.now()
        offset = now - datetime.timedelta(hours=12)  # 12 hours ago
        if self.updated <= offset:
            self.do_match()
        else:
            print 'already updated'

