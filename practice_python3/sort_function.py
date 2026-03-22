#Start
history = []

#Collect the input
while True:
    try:
        value = int(input("Enter the number: "))
        history.append(value)

    except ValueError:
        if history:
            print(f"Error. The entered numbers are: {sort(history)} ") 
        break