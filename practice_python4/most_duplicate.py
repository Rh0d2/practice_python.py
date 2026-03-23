history = []

while True:
    try:
        user_input = int(input("Enter the number: "))
        history.append(user_input)

    except ValueError:
        if history:
            most_duplicate = max(set(history), key = history.count)

            if history.count(most_duplicate) > 1:
                print(f"The most duplicated value is: {most_duplicate}")
            else:
                print("No duplicates were found.")
        
        # 3. Break must be inside 'except' but outside 'if history' to stop the loop
        break