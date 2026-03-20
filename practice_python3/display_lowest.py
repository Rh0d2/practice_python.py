history = []


while True:
    try:
        val = int(input("Enter the number: "))
        history.append(val)

    except ValueError:
        if history:
            print(f"Error! The lowest number is: {min(history)}")
        break
