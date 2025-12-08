def describe_age(a): 
    return "You're a(n) "+("kid"if a<13 else"teenager"if a<18 else"adult"if a<65else"elderly")
