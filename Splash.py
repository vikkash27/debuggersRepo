import requests
import json
import time
import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Retrieve the value of a key
KEY = os.getenv("KEY")
debug = os.getenv("DEBUG")

#KEY = "AIzaSyA3dsSFAb8rvjSBdZ__WLDYwhTYKEfWpNw"
GEMINI_ENDPOINT = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent"


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

name = input("What is your name? ")
archetype = input("""
                  Choose your developer archetype:
                   [Backend Sage, Frontend Sorcerer, DevOps Monk, QA Rogue] 
                  """)
# Sample Archetype Prompts
archetype_prompts = {
    "Backend Sage": f"Create a story in less than 50 words where a Backend Sage must debug a mythical API that controls an ancient city's defenses. my player's name is {name}.",
    "Frontend Sorcerer": f"Write a story in less than 50 words about a Frontend Sorcerer who is designing an enchanted interface to help citizens navigate a magical library. my player's name is {name}",
    "DevOps Monk": f"Tell a story in less than 50 words where a DevOps Monk is tasked with maintaining the flow of a mystical CI/CD pipeline that powers a kingdom. my player's name is {name}",
    "QA Rogue": f"Generate a story in less than 50 words where a QA Rogue must track down a critical bug hidden in a sprawling forest of code.with the name of my player's name is {name}"
}

# Function to simulate a typing effect
def typewriter_effect(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  # To move to the next line after the text is printed

# Function to generate the event based on player archetype
def generate_event(player):
    prompt = archetype_prompts.get(player['archetype'], "Create a generic coding adventure. Provide a short response")

    payload = {
        "contents": [
            {"parts": [{"text": prompt}]}
        ]
    }

    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(
        f"{GEMINI_ENDPOINT}?key={KEY}",
        headers=headers,
        data=json.dumps(payload)
    )

    if response.status_code == 200:
        content = response.json()
        return content['candidates'][0]['content']['parts'][0]['text']
    else:
        return "An error occurred while generating the story. Please try again."

# Function to simulate player decisions and consequences
def present_scenario(player, level):
    event_story = generate_event(player)
    typewriter_effect(f"\nLevel {level}:")
    typewriter_effect(event_story)
    
    # Simulate different choices for each level
    choices = {
        1: ["Investigate the source of the bug", "Ignore and continue", "Report to the team"],
        2: ["Fix the interface design", "Skip the optimization task", "Ask for assistance from a mentor"],
        3: ["Monitor the CI/CD pipeline", "Ignore the logs", "Push without testing"],
        4: ["Search the forest for the bug", "Give up and return to base", "Wait for help from others"],
        5: ["Prepare a deployment plan", "Attempt a quick fix", "Start a new project without testing"]
    }

    # The player selects an option
    typewriter_effect("\nChoose your action:")
    for idx, choice in enumerate(choices[level], 1):
        typewriter_effect(f"{idx}. {choice}")

    choice = int(input("Enter your choice (1-3): "))
    
    # Consequences based on choice
    if (level == 1 and choice == 1) or (level == 2 and choice == 1) or (level == 3 and choice == 1) or (level == 4 and choice == 1) or (level == 5 and choice == 1):
        typewriter_effect("Good choice! You gain some experience.")
        player['skill_points'] += 5  # Positive outcome
    else:
        typewriter_effect("Bad choice! You lose health.")
        player['health'] -= 20  # Negative outcome

    # Display current status
    typewriter_effect(f"\nCurrent Health: {player['health']} | Skill Points: {player['skill_points']}")
    if player['health'] <= 0:
        typewriter_effect("\nYou have lost all your health. Game over!")
        return False
    return True

# Main game loop
def game_loop():
    player = {
        "name": name,
        "archetype": archetype,  # This can be customized
        "health": 100,
        "energy": 50,
        "skill_points": 10
    }

    typewriter_effect(f"Welcome, {player['name']}!\nYour adventure as a {player['archetype']} begins...\n")
    
    for level in range(1, 6):  # 5 levels
        if not present_scenario(player, level):
            break  # End game if player loses all health

    if player['health'] > 0:
        typewriter_effect("\nCongratulations! You've completed all levels.")
    else:
        typewriter_effect("\nGame Over.")

# Start the game
game_loop()