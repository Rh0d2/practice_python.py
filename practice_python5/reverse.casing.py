print("This code will reverse then case your name")
user_name = str(input("Please enter your name in incorrect casing: "))

name = user_name.swapcase()

print(f"Hi, {name}!")