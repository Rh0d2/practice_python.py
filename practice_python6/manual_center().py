# This program does the same job as center()
user_text = input("Enter text: ")
width = int(input("Enter total width: "))

spaces_needed = width - len(user_text)

if spaces_needed > 0:
    left_spaces = spaces_needed // 2
    right_spaces = spaces_needed - left_spaces
    result = (" " * left_spaces) + user_text + (" " * right_spaces)
else:
    result = user_text

print(f"'{result}'")