# Start
History = []

# This loop runs forever UNTIL the break command is hit
while True:
    try:
        # 1. Ask for input INSIDE the loop
        # If the user types "abc", this line triggers a "ValueError" immediately
        val = int(input("Please enter a number: "))
        
        # 2. Logic to check for duplicates
        if val in History:
            print(f"{val} is Duplicate")
        else:
            print(f"{val} is Unique")

    except ValueError:
        print("Input is invalid. Stopping...")
        break  # <--- THIS IS WHAT STOPS THE LOOP