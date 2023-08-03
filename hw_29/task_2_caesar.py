def encode(message: str, key: int) -> str:
    encode_message = ""

    for char in message:
        if char.isalpha():
            offset = ord('A') if char.isupper() else ord('a')
            encode_char = chr((ord(char) - offset + key) % 26 + offset)
            encode_message += encode_char
        else:
            encode_message += char

    return encode_message


def decode(message: str, key: int) -> str:
    decode_message = ""

    for char in message:
        if char.isalpha():
            offset = ord('A') if char.isupper() else ord('a')
            decode_char = chr((ord(char) - offset - key) % 26 + offset)
            decode_message += decode_char
        else:
            decode_message += char

    return decode_message