#the interest function takes in 3 values. It multiplies and adds them to the regular var, then rounds and appends it to an array. Then the next for loop does the same, but doesn't add it to compound. It then returns the 
#total
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
