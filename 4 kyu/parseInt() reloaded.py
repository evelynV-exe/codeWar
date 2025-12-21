def parse_int(string):
    current = result = 0
    units = {
        "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
        "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
        "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13,
        "fourteen": 14, "fifteen": 15, "sixteen": 16, "seventeen": 17,
        "eighteen": 18, "nineteen": 19}
    tens = {
        "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50,
        "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90}
    scales = {"hundred": 100, "thousand": 1000, "million": 1000000}

    
    for i in string.replace("-", " ").split():
        if i in units:
            current += units[i]
        elif i in tens:
            current += tens[i]
        elif i == "hundred":
            current *= 100
        elif i in scales:
            current *= scales[i]
            result += current
            current = 0
    return result + current

string = "one"

print(parse_int(string))
