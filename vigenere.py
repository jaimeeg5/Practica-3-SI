alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
text = "mvltykycmjfqlu"
key = "URJC"

# Extended key
r_key = ""
counter = 0
for letter in text:
    r_key += key[counter]
    counter += 1
    counter = counter % len(key)

def decypher(text, r_key):

    translation = ""
    for x in range(len(text)):
        aux = r_key[x]
        # Key index so we can search in the table
        aux_index = alphabet.index(aux)
        # Index of the letter in the alphabet
        aux2_index = alphabet.index(text[x])
        # We calculate the distance between the key index and the index of the letter in the original alphabet
        if aux2_index < aux_index:
            # We have to adjust the index of the letter if its lower than the key index
            aux2_index += 52
        # This distance represents the index of the letter in the key index row of the Vigenère table
        # This way we don´t need to create the table
        dist = aux2_index - aux_index

        result = alphabet[dist]
        translation += result
    return translation

def cypher(text, r_key):

    translation = ""
    for x in range(len(text)):
        aux = r_key[x]
        # Key index
        aux_index = alphabet.index(aux)

        ind = (alphabet.index(text[x]) + aux_index) % 52

        result = alphabet[ind]
        translation += result
    return translation

print(decypher(text, r_key))
print(cypher("sECREtPAsswOrD", r_key))