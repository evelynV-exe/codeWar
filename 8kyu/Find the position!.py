def position(letter):
    return ord(letter.lower()) - ord('a') + 1

print(position('a'))