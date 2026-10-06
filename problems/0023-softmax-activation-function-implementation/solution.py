import math

def softmax(scores: list[float]) -> list[float]:
    # Your code here
    maxi = max(scores)

    exp_scores = [
        math.exp(score - maxi)
        for score in scores
        ]
    total = sum(exp_scores)

    result = [score / total for score in exp_scores]

    return result