user_text = input("Enter text: ")
width = int(input("Enter total number of characters: "))

if len(user_text) < width:
    result = user_text + (" " * (width - len(user_text)))
else:
    result = user_text

print(f"'{result}'")