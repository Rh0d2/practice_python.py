# This program does the same job as capitalize()
user_text = input("Enter text: ")
result = ""

for i in range(len(user_text)):
    ch = user_text[i]

    if i == 0:
        if 'a' <= ch <= 'z':
            result += chr(ord(ch) - 32)
        else:
            result += ch
    else:
        if 'A' <= ch <= 'Z':
            result += chr(ord(ch) + 32)
        else:
            result += ch

print(result)