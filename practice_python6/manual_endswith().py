user_input = input("Enter your text: ")
suffix = input("Enter suffix: ")

if user_input[-len(suffix):] == suffix:
    print(True)
else:
    print(False)