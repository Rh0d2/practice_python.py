print("This program will convert you name into pascal casing.")

user_name = str(input("Enter your name: "))

name = user_name.title().replace(" ", "")

print(f"Hi, {name}!")
