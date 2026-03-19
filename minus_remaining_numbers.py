#Start
val = 0

#Collect numbers
num1 = int(input("Enter your first number: "))
#Remaining numbers
for i in range(9):
    remaining_num = int(input(f"Enter the remaining numbers {i + 1}: "))
    val += remaining_num

#Logic
result = (num1 - val)

#print
print(num1, "subtract to", val, "is", result)