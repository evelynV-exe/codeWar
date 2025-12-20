MORSE_CODE = MORSE_CODE = {
    ".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E",
    "..-.": "F", "--.": "G", "....": "H", "..": "I", ".---": "J",
    "-.-": "K", ".-..": "L", "--": "M", "-.": "N", "---": "O",
    ".--.": "P", "--.-": "Q", ".-.": "R", "...": "S", "-": "T",
    "..-": "U", "...-": "V", ".--": "W", "-..-": "X", "-.--": "Y",
    "--..": "Z",
    "-----": "0", ".----": "1", "..---": "2", "...--": "3", "....-": "4",
    ".....": "5", "-....": "6", "--...": "7", "---..": "8", "----.": "9"
}

def possible_words(morse_str):
    memo = {}

    def dfs(s):
        if s in memo:
            return memo[s]
        if not s:
            return {""}
        
        results = set()

        for code, letter in MORSE_CODE.items():
            if s.startswith(code):
                for rest in dfs(s[len(code):]):
                    results.add(letter + rest)
        memo[s] = results
        return results
    
    return dfs(morse_str)

print(possible_words("...."))