letters_of_vowes = "aeiouAEIOU"

word = "Hello, World!" # output: 3
word1 = "Aditya" # output: 3

def count_vowes(word: str) -> int:
    return sum([1 for ch in word if ch in letters_of_vowes])
    # return [ch in letters_of_vowes for ch in word].count(True)

print(count_vowes(word)) # output: 3
print(count_vowes(word1)) # output: 3


