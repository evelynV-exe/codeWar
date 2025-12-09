def is_uppercase(inp):
    return inp.isupper() or not any(c.isalpha() for c in inp)
