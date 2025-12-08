def reverse_words(text):
    words = text.split(" ")
    solution = []
    for w in words:
        solution.append(w[::-1])
    return " ".join(solution)
