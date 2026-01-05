import re

def flesch_kincaid(text):
    text = text.lower()
    text = re.sub(r'\.\.\.+', '', text)
    text = re.sub(r"[-–—'’()]",  '', text)
   
    #sentence count
    sentences = max(1, len(re.findall(r'[.!?]', text)))

    text = text.replace(".", '')
    text = re.sub(r'\s+', ' ', text).strip()

    #words
    words = text.split()
    words_length = len(words)

    #syllables 
    vowel = "aeiou"
    syl = 0

    for word in words:
        prev_char_vowel = False
        word_syl =0

        for char in word:
            if char in vowel:
                if not prev_char_vowel:
                    word_syl += 1
                prev_char_vowel = True
            else:
                prev_char_vowel = False

        if word.endswith("e") and not word.endswith("le") and word_syl > 1:
            word_syl -= 1

        if word.endswith("ness"):
            word_syl += 1
    
        syl += max(word_syl, 1)

    fk = (0.39 * (words_length / sentences)) + (11.8 * (syl / words_length)) - 15.59

    return round(fk, 2)
