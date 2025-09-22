#the michaelPays function takes in 1 value, cost, and checks to see if it's less than 5, then Michael just pays. If it is more than 5 but less than 30, because the other person will pay 1/3 of the total cost, but only a max of $10.
#Finally, if the cost goes over $30, then Michael pays the remaining after $10 is subtracted.
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
