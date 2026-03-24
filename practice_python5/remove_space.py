# User instruction
print("Please Enter your name with several space characters in the beginning")

# Collect username
user_name = str(input("Enter your name: "))

# Remove space
name = user_name.lstrip()

print(f"Hi, {name}")