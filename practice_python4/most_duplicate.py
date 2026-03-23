history = []

while True:
    try:
        user_input = int(input("Enter the number: "))
        history.append(user_input)

    except ValueError:
        if history: 
            most_duplicate = list(set([num for num in history if history.count(num) >= 2]))
        
        if most_duplicate:
            print(f" The most duplicated value is: {max(most_duplicate)}")
        break