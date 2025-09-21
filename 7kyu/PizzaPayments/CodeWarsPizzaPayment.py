
def michaelPays(cost):
    if cost < 5:
        return round(cost, 2)
    elif cost >= 5 and cost <= 30:
        result = cost * (1/3)
        result = cost - result
        return round(result, 2)
    else:
        result = cost - 10
        return round(result, 2)
print(michaelPays(40))