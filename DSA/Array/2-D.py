# 2-D Array....
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

# Access element...
print("Element at row 1, col 2:",matrix[1][0])

# Loop throgh 2-D array
for row in matrix:
    for val in row:
        print(val,end=" ")
    print()

