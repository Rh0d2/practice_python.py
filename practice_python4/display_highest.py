history = []

while True:
    try:
        user_input = int(input("Enter the number: "))
        history.append(user_input)
    
    except ValueError:
        if history:
            print(f"The highest value is {max(history)}")
        break