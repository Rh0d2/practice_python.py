#Start
result = 0
numbers = []

    #Collect numbers
for i in range(100):
    val = int(input(f"Enter the number {i + 1}: "))

    #Count numbers except ending with 0
    if val % 10 != 0:
         result += 1

print(f"Numbers starting from 0 to 100 except numbers ending in zero are {result}")
