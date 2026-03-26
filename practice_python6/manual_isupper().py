user_input = input("Enter the text: ")

all_upper = True

for ch in user_input:
    if 'a' <= ch <= 'z':
        all_upper = False

print(all_upper)