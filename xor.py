def XOR(text, key):
    result = ""
    for i in range(len(text)):
        result = result + chr(ord(text[i]) ^ ord(key[i % len(key)]))
    print(result)
    return

XOR("({!+8b*+", "XOR")
XOR("p4ssw0rd", "XOR")
