print("This program will convert you name into snake casing.")

user_name = str(input("Enter your name: "))

name = user_name.lower().replace(" ","_")

print(f"Hi, {name}!")
