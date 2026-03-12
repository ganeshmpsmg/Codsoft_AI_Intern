# Codsoft_AI_Intern  chatbot.py
📄 README.md
# 🤖 Rule-Based Chatbot (Python)

A simple **Rule-Based Chatbot** built using **Python** as part of the **CodSoft AI Internship - Task 1**.

The chatbot interacts with users through **pattern matching using Regular Expressions** and responds with predefined messages.

---

## 📌 Project Overview

This chatbot can:

✔ Greet users  
✔ Respond to basic questions  
✔ Tell jokes  
✔ Show current **time and date**  
✔ Detect user emotions  
✔ Provide fallback responses when input is not understood  

The chatbot runs in the **command line interface (CLI)**.

---

## 🛠 Technologies Used

- Python
- Regular Expressions (`re`)
- Random module
- Datetime module

All libraries used are **built-in Python libraries**, so no additional installations are required.

---

## 📂 Project Structure


chatbot/
│
├── chatbot.py # Main chatbot program
├── README.md # Project documentation
└── requirements.txt # Dependencies


---

## ▶️ How to Run the Project

### 1️⃣ Clone the repository


git clone https://github.com/ganesmpsmg/chatbot.git


### 2️⃣ Navigate to the project folder


cd chatbot


### 3️⃣ Run the chatbot


python chatbot.py


---

## 💬 Example Chat


You: hello
Bot: Hello! How can I help you?

You: tell me a joke
Bot: Why did the computer get cold? It forgot to close Windows!

You: what is ai
Bot: AI is machines simulating human intelligence.

You: bye
Bot: Goodbye! Have a great day!


---

## 🧠 How It Works

The chatbot uses **pattern matching** with the `re` module.

Example rule:

```python
(r"hi|hello|hey", ["Hello!", "Hey there!", "Hi!"])

When a user types a message, the chatbot:

Checks if the message matches a pattern

Selects a response randomly

Displays the reply to the user

📌 Internship Task

This project was developed as part of:

CodSoft AI Internship

Task 1: Rule-Based Chatbot

👨‍💻 Author

Ganesh MP

Engineering Student | AI & Machine Learning Enthusiast

GitHub: https://github.com/ganeshmpsmg    
