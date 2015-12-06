from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .models import UserAnswer
from .models import score_importance

@receiver(pre_save, sender=UserAnswer)
def update_user_answer_score(sender, instance, *args, **kwargs):
    my_points = score_importance(instance.my_answer_importance)
    instance.my_points = my_points
    their_points = score_importance(instance.their_answer_importance)
    instance.their_points = their_points

# pre_save.connect(update_user_answer_score, sender=UserAnswer)

# def update_user_answer_score(sender, instance, created, *args, **kwargs):
#     if created:
#         if instance.my_points == -1:
#             my_points = score_importance(instance.my_answer_importance)
#             instance.my_points = my_points
#             instance.save()
#     
#         if instance.their_points == -1:
#             their_points = score_importance(instance.their_answer_importance)
#             instance.their_points = their_points
#             instance.save()
 
# post_save.connect(update_user_answer_score, sender=UserAnswer)
