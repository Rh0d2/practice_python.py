# This program will do the similar function as lstrip()
print("Please enter your name with space characters first")
user_name = str(input("Enter your name: "))

import re
name = re.sub('^ +', '', user_name).title()

print(f"Hi, {name}!")