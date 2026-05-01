# ########################################### #
# Ensure you have the library installed:      #
# pip uninstall pycrypto (to avoid conflicts) #
# pip install pycryptodome                    #
###############################################

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def fromEncrypted(text, key, iv):
    encoded_text = bytes.fromhex(text)
    key_bytes = key.encode('utf-8')
    iv_bytes = iv.encode('utf-8')

    cipher = AES.new(key_bytes, AES.MODE_CBC, iv_bytes)
    cipher_result = cipher.decrypt(encoded_text)
    result_unpadded = unpad(cipher_result, AES.block_size)

    result = result_unpadded.decode('utf-8')
    print(result)
    return

def toEncrypted(text, key, iv):
    encoded_text = text.encode('utf-8')
    key_bytes = key.encode('utf-8')
    iv_bytes = iv.encode('utf-8')

    cipher = AES.new(key_bytes, AES.MODE_CBC, iv_bytes)
    padded_text = pad(encoded_text, AES.block_size)
    cipher_result = cipher.encrypt(padded_text)

    result = cipher_result.hex().upper()
    print(result)
    return

fromEncrypted("F55228945ACF1A291DB0C84409852406", "SeguridadInforma", "SeguridadInforma")
toEncrypted("URJC{L4stP4ss}", "SeguridadInforma", "SeguridadInforma")