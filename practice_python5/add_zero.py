print("Please enter number in range of 1-1000. Max of 6 digit")

user_input = input("Enter the number: ")
num = int(user_input)

if 0 <= num <= 1000:
    collected_num = user_input.zfill(6)
    print(f"Your number is: {collected_num}")
else:
    print("Invalid input!")