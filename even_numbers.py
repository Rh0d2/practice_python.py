#Start
numbers = []

#Collect numbers
for i in range(10):
    val = int(input(f"Enter number {i + 1}: "))
    #Even logic
    if val % 2 == 0:
        numbers.append(val)

print(f"All the even numbers starting from 0 to 10 are {numbers}")