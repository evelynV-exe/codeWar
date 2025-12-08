def DNA_strand(dna):
    solution = ""
    for char in dna:
        if char == 'A':
            solution += "T"
        elif char == "T":
            solution += "A"
        elif char == "C":
            solution += "G"
        elif char == "G":
            solution += "C"
    return solution
