#start 
total_odd = 0
numbers = []

#collect numbers
for i in range(10):
    val = int(input(f"Enter number {i + 1}: "))
    #Logic to determine odd numbers
    if val % 2 != 0:
        total_odd += 1

print(f"There are {total_odd} odd numbers")
