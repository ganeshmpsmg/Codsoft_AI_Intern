"""
CODSOFT AI Internship - Task 1
Rule-Based Chatbot
Run: python chatbot.py
"""

import re
import random
import datetime

RULES = [
    (r"hi|hello|hey|good morning|good afternoon|good evening|hi there",
     ["Hello! How can I help you?",
      "Hey there!",
      "Hey! I'm here to assist you!"]),

    (r"how are you",
     ["I'm doing great!",
      "All good, thanks for asking!",
      "Don't worry I am fine."]),

    (r"your name|who are you",
     ["I'm Gani.",
      "Call me GoldGani!"]),

    (r"who made you|who created you",
     ["A skill eager man built me!"]),

    (r"what can you do|help",
     ["I can chat, tell jokes, share time/date and more!"]),

    (r"time",
     [f"Current time: {datetime.datetime.now().strftime('%I:%M %p')}"]),

    (r"date|today",
     [f"Today: {datetime.datetime.now().strftime('%A, %B %d, %Y')}"]),

    (r"joke",
     ["Why don't scientists trust atoms? They make up everything!",
      "Why did the AI go to school? To improve its neural network!",
      "When the internet is slow, everyone suddenly becomes a network engineer!",
      "Why did the computer get cold? It forgot to close Windows!"]),

    (r"i'm (good|great|happy|fine|awesome|excellent|amazing)",
     ["That's great to hear!",
      "That's nice to hear!",
      "That’s wonderful to hear!",
      "Good to know!"]),

    (r"i'm (sad|bad|tired|bored)",
     ["Sorry to hear that. Hope things get better!"]),

    (r"thank|thanks",
     ["You're welcome!",
      "Happy to help!"]),

    (r"weather",
     ["I don't have live weather updates. Please check weather.com!"]),

    (r"what is ai|artificial intelligence",
     ["AI is machines simulating human intelligence."])
]


def get_response(user_input):
    for pattern, responses in RULES:
        if re.search(pattern, user_input, re.IGNORECASE):
            return random.choice(responses)

    return random.choice([
        "I didn't understand that. Can you rephrase? ",
        "Hmm, I'm not sure. Try asking something else!",
        "Sorry, I didn’t understand that. Could you rephrase?",
        "I’m not sure I understood. Can you say it differently?",
        "Could you please explain that in another way?"
    ])


print("=" * 45)
print(" GANI — CODSOFT AI Internship Task 1")
print("=" * 45)
print("Type anything to chat. Type 'bye' to exit.\n")

while True:
    user = input("You: ").strip()

    if not user:
        continue

    if re.search(r"bye|goodbye|exit|quit", user, re.IGNORECASE):
        print("bot: Goodbye! Have a great day!")
        break

    reply = get_response(user)
    print(f"Bot: {reply}\n")