from datetime import datetime

# Step 1: Ask for the user's name
name = input("What is your name? ")

# Step 2: Ask for the user's year of birth
year_of_birth = int(input("What is your year of birth? "))

# Step 3: Calculate the user's age
current_year = datetime.now().year
age = current_year - year_of_birth

# Step 4: Print the message
print(f"Hello {name}, I can see you are {age} years old.")
