user_input = input("Enter your text: ")
result = ""

for ch in user_input:
    if 'A'<= ch <= 'Z':
        result += chr(ord(ch) + 32)
    else:
        result += ch

print(result)