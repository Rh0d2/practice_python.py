# This program does the same job as title()
user_text = input("Enter text: ")
result = ""
new_word = True

for ch in user_text:
    if ch == " ":
        result += ch
        new_word = True
    else:
        if new_word:
            if 'a' <= ch <= 'z':
                result += chr(ord(ch) - 32)
            else:
                result += ch
            new_word = False
        else:
            if 'A' <= ch <= 'Z':
                result += chr(ord(ch) + 32)
            else:
                result += ch

print(result)