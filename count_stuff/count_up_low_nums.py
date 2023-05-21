
line = "Hello123 , I am GEEKyboy"
line2 = "Hello, World"

def count_suff(text: str) -> tuple[int, int, int]:
    return sum(1 for char in text if char.isupper()), sum(1 for char in text if char.islower()), sum(1 for char in text if char.isdigit())

print(count_suff(line)) # output: (6, 10, 3)
print(count_suff(line2)) # output: (2, 8, 0)

u, l, d = count_suff(line)

print(f"""
        Uppercase: {u}
        Lowercase: {l}
        Digits: {d}
      """)

# output line:
"""
Uppercase: 6
Lowercase: 10
Digits: 3
"""
