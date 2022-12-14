# generate lists with range functions
numbers = list(range(1,11))
print(numbers)

# something more about pop method 
numbers = list(range(1,11))
popped_item=numbers.pop()
print(numbers)

# index method
# numbers = list(range(1,11))
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 5, 7, 8, 1]
print(numbers.index(1, 11))

# pass list to a function
def negative_list(l):
    negative=[]
    for i in l:
        negative.append(-i)
    return negative
print(negative_list(numbers))
