import hashlib
p="326f13e25448c99ccae78b0afa1c84e6fae2d8a587976df3a86628ae"
your_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
complete_list = []
from itertools import chain, product
def bruteforce(charset, maxlength):
    return (''.join(candidate)
        for candidate in chain.from_iterable(product(charset, repeat=i)
        for i in range(1, maxlength + 1)))
print(list(bruteforce(your_list,3)))
for attempt in bruteforce(your_list,3):
    # match it against your password, or whatever
    if hashlib.sha224(attempt.encode()).hexdigest() == p:
        print("Je hebt het wachtwoord gevonden! Het was:", attempt)
        break
    else:
        print("joj")
