#Start
result = 0

#Collect numbers
for i in range(10):
    val = int(input(f"Enter your number {i + 1}: "))
    #Logic
    if val % 2 == 0:
      result += 1

#Print
print(f"The total of even numbers are {result}: ")
