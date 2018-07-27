def sum_of_middle_three(score1, score2, score3, score4, score5):
    low = min(score1, score2, score3, score4, score5)
    high = max(score1, score2, score3, score4, score5)
    return score1 + score2 + score3 + score4 + score5 - low - high
def convert_to_numeric(score):
    """
    Convert the score to a numerical type.
    """
    converted_score = float(score)
    return converted_score
def score_to_rating_string(score):
    if score < 1:
        return "Terrible"
    if score < 2:
        return "Bad"
    if score < 3:
        return "OK"
    if score < 4:
        return "Good"
    if score < 5:
        return "Excellent"
    return ""
def scores_to_rating(score1, score2, score3, score4, score5):
    """
    turns 5 scores into a rating string
    """

    #converting scores to same format
    score1 = convert_to_numeric(score1)
    score2 = convert_to_numeric(score2)
    score3 = convert_to_numeric(score3)
    score4 = convert_to_numeric(score4)
    score5 = convert_to_numeric(score5)

    #calculating the mean
    mean = sum_of_middle_three(score1, score2, score3, score4, score5)/3

    #getting the string representation of the rating
    rating = score_to_rating_string(mean)

    return rating

print(scores_to_rating("1", "3.0", 2, 2, 3))
