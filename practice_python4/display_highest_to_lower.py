history = []

while True:
    try:
        user_input = int(input("Enter the number: "))
        history.append(user_input)
        sorted_number = sorted(history, reverse=True)

    except ValueError:
        if sorted_number:
            print(sorted_number)
        break