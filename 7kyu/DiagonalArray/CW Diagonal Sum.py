#diagonalSum takes in an array of numbers. Then it uses the sum function to add the values together for however long the array is.
def diagonalSum(array):
    return sum(array[i][i] for i in range(len(array)))
print(diagonalSum(""))

