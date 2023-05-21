letters_of_vowes = "aeiouAEIOU"

word = "Hello, World!" # output: 3
word1 = "Aditya" # output: 3

print([ch in letters_of_vowes for ch in word].count(True))
print([ch in letters_of_vowes for ch in word1].count(True))
