from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import Match


class MatchManagerTests(TestCase):
    def test_get_or_create_match_is_symmetric(self):
        user_model = get_user_model()
        user_a = user_model.objects.create_user(username="user_a", password="pass1234")
        user_b = user_model.objects.create_user(username="user_b", password="pass1234")

        match_ab, created_ab = Match.objects.get_or_create_match(user_a=user_a, user_b=user_b)
        self.assertTrue(created_ab)
        self.assertEqual(Match.objects.count(), 1)

        match_ba, created_ba = Match.objects.get_or_create_match(user_a=user_b, user_b=user_a)
        self.assertFalse(created_ba)
        self.assertEqual(match_ab.pk, match_ba.pk)
        self.assertEqual(Match.objects.count(), 1)
