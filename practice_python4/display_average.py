history = []

while True:
    try: 
        user_input = int(input("Enter the number: "))
        history.append(user_input)
    
    except ValueError:
        if history:
            print(f"The average of the value is: {sum(history) / len(history)}")
        break