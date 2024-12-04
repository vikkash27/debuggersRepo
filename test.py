from datetime import datetime
import sys

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
                🌐 Your Journey Awaits... 🌐
------------------------------------------------------------
 [New Game]          [Load Game]          [Settings]
      
""")

def title_screen_options():
	#Allows the player to select the menu options, case-insensitive.
	option = input("> ")
	if option.lower() == ("play"):
		pass
		# setup_game()
	elif option.lower() == ("quit"):
		sys.exit()
	elif option.lower() == ("help"):
		pass	
	while option.lower() not in ['play', 'help', 'quit']:
		print("Invalid command, please try again.") 
		option = input("> ")
		if option.lower() == ("play"):
			pass
		elif option.lower() == ("quit"):
			sys.exit()
		elif option.lower() == ("help"):
			pass

# # Step 1: Ask for the user's name
# name = input("What is your name? ")

# # Step 2: Ask for the user's year of birth
# year_of_birth = int(input("What is your year of birth? "))

# # Step 3: Calculate the user's age
# current_year = datetime.now().year
# age = current_year - year_of_birth

# # Step 4: Print the message
# print(f"Hello {name}, I can see you are {age} years old.")
