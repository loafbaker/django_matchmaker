from questions.models import UserAnswer


def get_points(user_a, user_b):
    a_answers = UserAnswer.objects.filter(user=user_a)
    b_answers = UserAnswer.objects.filter(user=user_b)
    a_total_awarded = 0
    a_points_possible = 0
    num_question = 0
    for a in a_answers:
        for b in b_answers:
            if a.question.id == b.question.id:
                num_question += 1
                a_pref = a.their_answer
                b_answer = b.my_answer
 
                if a_pref == b_answer:
                    a_total_awarded += a.their_points
                a_points_possible += a.their_points
            print '%s has awarded %s points of %s to %s' %  (user_a, a_total_awarded, a_points_possible, user_b)

    percent = a_total_awarded / float(a_points_possible)
    # Avoid zero division
    if percent < 1e-6:
        percent = 1e-6
    return percent, num_question


match1, n = get_points(david, jmchen)
match2, n = get_points(jmchen, david)

match_percentage = (match1 * match2) ** (1./n)
