#The pattern function takes in 1 value n and checks to see if it is less than or equal to 0, and if it is, then it returns an empty string. Then whatever number the user inputs is taken and multiplied by the number they added to create a pattern
#After that, it is added to a list and then returned with a new line indicator.
def pattern(n: int) -> str:
    if n <= 0:
        return ""
    result = []
    for i in range(1, n + 1, 2):
        result.append(str(i) * i)
    return "\n".join(result)
      
print(pattern(5))

