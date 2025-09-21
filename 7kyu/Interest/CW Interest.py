from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_DOWN
def interest(p, r, n):
    total = []
    regular = p
    compoundPrincipal = p
    compoundInterest = r
    for i in range(n):
        regular += p * r
    regular = round(regular)
    total.append(int(regular))
    for i in range(n):
        compound = compoundPrincipal * compoundInterest 
        print(compoundPrincipal)
        compoundPrincipal += compound
        print(compoundPrincipal)
    compoundPrincipal = round(compoundPrincipal)
    total.append(int(compoundPrincipal))
    return total
print(interest(303, .9, 47))