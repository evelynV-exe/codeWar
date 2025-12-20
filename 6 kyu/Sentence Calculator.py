def letter_to_number(s):
    total = 0

    for ch in s:
        if 'a' <= ch <= 'z':
            value = ord(ch) - ord('a') + 1
        elif 'A' <= ch <= 'Z':
            value = (ord(ch) - ord('A') + 1) * 2
        elif '0' <= ch <= '9':
            value = int(ch)

        total += value
    
    return total

letter_to_number("I Love You")