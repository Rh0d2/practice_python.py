#Start
numbers = []

#Collect numbers
for i in range(101):
    val = int(input(f"Enter number {i + 1}: "))
    #Even logic
    if val % 2 == 0:
        numbers.append(val)

print(f"All the even numbers starting from 0 to 101 are {numbers}")