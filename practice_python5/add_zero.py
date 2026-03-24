print("Please enter number in range of 1-100. Max of 6 digit")

user_input = str(input("Enter the number: "))

for user_input in range(6):
    if user_input > 6:
        print("Error. 6 digit max only")
    else:
        print(f"Your official number is: {user_input.zfill(6)}")