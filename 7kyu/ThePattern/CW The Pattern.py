def pattern(n: int) -> str:
    if n <= 0:
        return ""
    result = []
    for i in range(1, n + 1, 2):
        result.append(str(i) * i)
    return "\n".join(result)
      
print(pattern(5))
