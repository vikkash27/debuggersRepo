import requests
import json


KEY = "AIzaSyA3dsSFAb8rvjSBdZ__WLDYwhTYKEfWpNw"
# Gemini API Key (replace with your actual key)
GEMINI_ENDPOINT = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent"

def generate_event(player):
    # Craft a prompt based on the player's archetype
    archetype_prompts = {
        "Backend Sage": "Create a story where a Backend Sage must debug a mythical API that controls an ancient city's defenses.",
        "Frontend Sorcerer": "Write a story about a Frontend Sorcerer who is designing an enchanted interface to help citizens navigate a magical library.",
        "DevOps Monk": "Tell a story where a DevOps Monk is tasked with maintaining the flow of a mystical CI/CD pipeline that powers a kingdom.",
        "QA Rogue": "Generate a story where a QA Rogue must track down a critical bug hidden in a sprawling forest of code."
    }
    prompt = archetype_prompts.get(player['archetype'], "Create a generic coding adventure.")

    # Prepare the payload for the API
    payload = {
        "contents": [
            {"parts": [{"text": prompt}]}
        ]
    }

    # Send the request to Gemini API
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(
        f"{GEMINI_ENDPOINT}?key={KEY}",
        headers=headers,
        data=json.dumps(payload)
    )

    if response.status_code == 200:
        # Parse and return the generated content
        content = response.json()
        return content['candidates'][0]['content']['parts'][0]['text']
    else:
        return "An error occurred while generating the story. Please try again."

# Example usage
player = {
    "name": "Alice",
    "archetype": "Backend Sage",
    "health": 100,
    "energy": 50,
    "skill_points": 10,
}

# Generate a dynamic event
event_story = generate_event(player)
print("Dynamic Story/Event:")
print(event_story)