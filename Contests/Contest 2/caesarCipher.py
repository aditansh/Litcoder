import sys

def decode(s, shift=4):
    result = ""

    for i in s:
        if i.isalpha():
            if i.isupper():
                result += chr((ord(i) + shift - 65) % 26 + 65)
            else:
                result += chr((ord(i) + shift - 97) % 26 + 97)
        else:
            result += i
    
    return result

s=input()
print(decode(s))