print("Please input your name with several space characters in the beginning")
user_name = str(input("Enter your name: "))

name = user_name.lstrip()

print(f"Hi, {name}")