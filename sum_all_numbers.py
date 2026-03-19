#start
total = 0

#Collect numbers
for i in range(10):
    val = float(input(f"Enter number {i + 1}: "))
    #sum logic
    total += val

print(f"Print the sum of all the numbers is {total}")