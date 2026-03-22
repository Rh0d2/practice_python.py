# Start
history = []
number = 0

# Collect inputs 10 times
for i in range(10):
    user_input = int(input(f"Enrter the number{i +1}: "))
    history.append(user_input)
    number = history
    duplicates = [num for num, freq in number.count() if  1]
print(duplicates)