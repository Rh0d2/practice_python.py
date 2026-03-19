#start 
total_odd = 0

#collect numbers

for i in range(10):
    val = int(input(f"Enter number {i + 1}: "))
    if val % 2 != 0:
        total_odd = val

print(f"There are {total_odd} odd numbers")
