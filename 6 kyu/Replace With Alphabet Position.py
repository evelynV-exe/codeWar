def alphabet_position(text):
    sentence = text.lower()
    position = []
    for char in sentence:
        if 'a' <= char <= 'z':
            position.append(str(ord(char) - ord('a') + 1))
    return " ".join(position)
text = "The sunset sets at twelve o' clock."

print(alphabet_position(text))