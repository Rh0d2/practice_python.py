#Start
numbers = []
final_list = []

#Collect numbers
for i in range(10):
    val = int(input(f"Enter the number{i + 1}: "))
    #Turn the entered numbers to list
    numbers.append(val)

for num in numbers:
    if numbers.count(num) == 1:
        final_list.append(num)

print(final_list)


