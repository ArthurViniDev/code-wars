def rot13(message: str) -> str:
    m13 = ''
    for l in message:
        if 'a' <= l <= 'z':
            m13 += chr((ord(l) - ord('a') + 13) % 26 + ord('a'))
        elif 'A' <= l <= 'Z':
            m13 += chr((ord(l) - ord('A') + 13) % 26 + ord('A'))
        else:
            m13 += l
    return m13
