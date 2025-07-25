def round_to_nearest_10000(n):
    return round(n / 10000) * 10000


def calculate_credit_limit(annual_income, credit_score):
    return round_to_nearest_10000(annual_income * (credit_score / 100) * 0.4)

def calculate_tenure(credit_score):
    if credit_score >= 80:
        return 4
    elif credit_score >= 75:
        return 3
    elif credit_score >= 70:
        return 2
    elif credit_score >= 65:
        return 1
    else:
        return 0.5

def calculate_interest_rate(credit_score):
    interest_rate = 20 - ((credit_score - 60) * 0.3)
    return float(max(10, round(interest_rate, 1)))