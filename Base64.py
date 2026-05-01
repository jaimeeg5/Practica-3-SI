import base64

def fromBase64(textBase64):
    textBase64Encoded = textBase64.encode('utf-8')
    result = base64.b64decode(textBase64Encoded).decode('utf-8')
    print(result)
    return

def toBase64(textBase64):
    textBase64Encoded = textBase64.encode('utf-8')
    result = base64.b64encode(textBase64Encoded).decode('utf-8')
    print(result)
    return

fromBase64("VVJKQ3tTTTRMTF9CNFMzXzY0fQ==")
toBase64("URJC{SM4LL_B4S3_64}")
