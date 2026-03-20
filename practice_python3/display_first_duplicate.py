#start
numbers = []
result = 0

#collect numbers
for i in range(10):
    val = int(input(f"Enter number {i + 1}: "))
    #Turn collected values into list
    numbers.append(val)
    #Remove duplicates
    result = list(dict.fromkeys(numbers))
print(result)
