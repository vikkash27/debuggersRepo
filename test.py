from datetime import datetime

print("""
============================================================
███████╗██╗   ██╗███╗   ██╗████████╗ █████╗ ██╗  ██╗       
██╔════╝██║   ██║████╗  ██║╚══██╔══╝██╔══██╗╚██╗██╔╝       
█████╗  ██║   ██║██╔██╗ ██║   ██║   ███████║ ╚███╔╝        
██╔══╝  ██║   ██║██║╚██╗██║   ██║   ██╔══██║ ██╔██╗        
██║     ╚██████╔╝██║ ╚████║   ██║   ██║  ██║██╔╝ ██╗       
╚═╝      ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝       
------------------------------------------------------------
                 Welcome to **Syntax Saga**                  
        An RPG Adventure Through the World of Code!          
============================================================

            🌟 Choose Your Developer Archetype 🌟
#    [1] Backend Sage - Master of APIs and Databases.
#    [2] Frontend Sorcerer - Weaver of Interfaces and UX.
#    [3] DevOps Monk - Keeper of CI/CD Rituals.
#    [4] QA Rogue - Hunter of Bugs and Breakpoints.

                🌐 Your Journey Awaits... 🌐
------------------------------------------------------------
 [New Game]          [Load Game]          [Settings]
      """)

# Step 1: Ask for the user's name
name = input("What is your name? ")

# Step 2: Ask for the user's year of birth
year_of_birth = int(input("What is your year of birth? "))

# Step 3: Calculate the user's age
current_year = datetime.now().year
age = current_year - year_of_birth

# Step 4: Print the message
print(f"Hello {name}, I can see you are {age} years old.")
