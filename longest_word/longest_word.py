words = ["aditya", "ayush"]

wordlist = [
    "Serendipity",
    "Quixotic",
    "Sesquipedalian",
    "Mellifluous",
    "Soliloquy",
    "Ephemeral",
    "Pulchritudinous",
    "Epiphany",
    "Equanimity",
    "Nebulous"
]

# one-liner
def oneliner(word_list: list[str]) -> str:
    return [word for word in word_list if len(word) == max(len(word) for word in word_list)][0]

# most effective way
def effective(word_list: list[str]) -> str:
    max_length = max(len(word) for word in word_list)
    return [word for word in word_list if len(word) == max_length][0]

print(oneliner(words)) # output: aditya
print(effective(words)) # output: aditya

print(oneliner(wordlist)) # output: Pulchritudinous
print(effective(wordlist)) # output: Pulchritudinous
