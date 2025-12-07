def abbrev_name (name):
    word = name.split()
    solution = ".".join(w[0].upper() for w in word)

    return solution

print(abbrev_name("Sam Harris"))
