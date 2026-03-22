# Start
history = []
number = 0

# Collect inputs 10 times
for i in range(10):
    user_input = int(input(f"Enrter the number{i +1}: "))
    # Turn collected inputs into list
    history.append(user_input)

    number = history

    #Collect the duplicated numbers only
    duplicates = list(set([num for num in history if history.count(num) > 1]))   

print(f"The duplicated numbers are: {duplicates}")