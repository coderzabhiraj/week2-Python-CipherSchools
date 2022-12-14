# list inside list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# 3 items ---> 3 list
# print(matrix[1])

for sublist in matrix: # 1 solution
    for i in sublist:
        print(i)

print(matrix[1][1]) # 2 solution


# type function
s = "string"
print(type(s))
print(type(matrix))