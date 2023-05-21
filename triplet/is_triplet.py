def is_triplet(a, b, c):
    return a**2 + b**2 == c**2

a, b, c = (3,4,5)
a2, b2, c2 = (8,10,18)

print(is_triplet(a, b, c)) # output: True
print(is_triplet(a2, b2, c2)) # output: False
