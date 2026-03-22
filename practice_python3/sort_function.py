# Start
history = []

# Collect the infinitely untill the ValueError
while True:
    try:
        value = int(input("Enter the number: "))
        # Store the user input in the list
        history.append(value)

    # Detect letters or symbols
    except ValueError:
        # Display the entered value from lowest to highest
        if history:
            print(f"Error. The entered numbers from lowest to highest are: {sorted(history)} ") 
        break