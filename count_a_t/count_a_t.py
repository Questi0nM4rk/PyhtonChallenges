

def easy_apr(text: str) -> tuple[int, int]:
    text = text.lower()
    return (text.count("t"), text.count("e"))


def next_apr(text: str) -> dict:
    text = text.lower()
    find = ["t", "e"]
    
    return {char: sum(char in word for word in text) for char in find}


with open("sample.txt", "r", encoding="utf-8") as f:
    lines = f.read()
    
    t, e = easy_apr(lines)
    print(f"t/T = {t}\n" +
          f"e/E = {e}")
    
    occurrences = next_apr(lines)
    print("Occurrences of 't':", occurrences["t"])
    print("Occurrences of 'e':", occurrences["e"])
    
    # output:
    """
    t/T = 39
    e/E = 57
    
    Occurrences of 't': 39
    Occurrences of 'e': 57
    """