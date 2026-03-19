#Start
number = 0

#Loop for <= 100
while number <= 100:
    #Check of number is ending with 0 or 5
    if number % 10 not in [0, 5]:
        print(number)
    #Inrement the number
    number += 1