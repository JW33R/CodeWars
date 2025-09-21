import math
def michealPays(cost):
    if cost < 5:
        return cost
    elif cost > 5:
        result = cost * (1/3)
        result = cost - result
        return round(result, 2)
print(michealPays(40))