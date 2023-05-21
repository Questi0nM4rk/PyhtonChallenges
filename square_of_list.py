numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
print(squares) # output: [1, 4, 9, 16, 25]

# for input of list:

print([int(x)**2 for x in input().split(",")])
# input: 1,2,3,4,5,6
# output: [1, 4, 9, 16, 25, 36]