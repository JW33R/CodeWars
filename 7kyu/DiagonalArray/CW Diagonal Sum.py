
def diagonalSum(array):
    return sum(array[i][i] for i in range(len(array)))
print(diagonalSum(""))
