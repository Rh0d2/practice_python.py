#This program will remove your set prefix
user_text = (input("Enter text: "))
prefix = (input("Enter the prefix to be removed: "))

if user_text.startswith(prefix):
    user_text = user_text[len(prefix):]

print(user_text)
