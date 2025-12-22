from collections import Counter
import string

def mix(s1, s2):
    # count the frequency of lowercase letters
    freq1 = Counter(ch for ch in s1 if ch in string.ascii_lowercase)
    freq2 = Counter(ch for ch in s2 if ch in string.ascii_lowercase)
    result = []

    for letter in string.ascii_lowercase:
        #max frequency
        c1 = freq1.get(letter, 0)
        c2 = freq2.get(letter, 0)
        maxChar = max(c1, c2)

        if maxChar > 1:
            if c1 >c2:
                prefix = "1:"
            elif c2 > c1:
                prefix = "2:"
            else:
                prefix = "=:"
            result.append(prefix + letter * maxChar)
        
        #sort the order
        def sortKey(x):
            letters = x.split(":")[1]
            return (-len(letters), x)
        
        result = sorted(result, key=sortKey)
    return "/".join(result)

s1 = "my&friend&Paul has heavy hats! &"
s2 = "my friend John has many many friends &"
freq = mix(s1, s2)

print("freq: ", freq)