alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
def decypher(text, despl):
    traduction = ""
    for letter in text:
        if letter in alphabet:
            auxIndex = (alphabet.index(letter) + despl)
            alphabetLetter = alphabet[auxIndex % 26]
            traduction += alphabetLetter
        else:
            traduction += letter
    return traduction

# Encoding and decoding are performed the same way using the same shift but with the sign reversed
def cypher(text, despl):
    print(decypher(text, -despl))
    return

def bruteforce(text):
    for n in range(26):
        print(decypher(text, n))
    return

bruteforce("ROGZZ3P4O_Q1J3")
cypher("URJCC3S4R_T1M3",3)