import hashlib

def crack(hash):
    for pin in range(10**5):
        candidate = str(pin).zfill(5)

        if hashlib.md5(candidate.encode()).hexdigest() == hash:
            return candidate
    return None

hash = "827ccb0eea8a706c4c34a16891f84e7b"

print(crack(hash))