from django.db.models import Q
from questions.models import Question, UserAnswer

def get_match(user_a, user_b):
    q1 = Q(useranswer__user=user_a)
    q2 = Q(useranswer__user=user_b)
    question_set = Question.objects.filter(q1 | q2).distinct()
    questions_in_common = 0
    a_points = 0
    b_points = 0
    a_total_points = 0
    b_total_points = 0
    for question in question_set:
        try:
            a = UserAnswer.objects.get(user=user_a, question=question)
        except:
            a = None
        try:
            b = UserAnswer.objects.get(user=user_b, question=question)
        except:
            b = None

        if a and b:
            questions_in_common += 1
            if a.their_answer == b.my_answer:
                b_points += a.their_points
            b_total_points += a.their_points

            if b.their_answer == a.my_answer:
                a_points = b.their_points
            a_total_points += b.their_points

    if questions_in_common > 0:
        a_decimal = a_points / float(a_total_points)
        b_decimal = b_points / float(b_total_points)
        if a_decimal < 1e-6:
            a_decimal = 1e-6
        if b_decimal < 1e-6:
            b_decimal = 1e-6
        match_percentage = (a_decimal * b_decimal) ** (1./questions_in_common)
        return match_percentage, questions_in_common
    else:
        return 0.0, 0
            

