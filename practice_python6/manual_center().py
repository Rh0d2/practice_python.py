# This program does the same job as swapcase()
user_text = input("Enter text: ")
result = ""

for ch in user_text:
    if 'A' <= ch <= 'Z':
        result += chr(ord(ch) + 32)
    elif 'a' <= ch <= 'z':
        result += chr(ord(ch) - 32)
    else:
        result += ch

print(result)