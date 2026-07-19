# CampusCare Mood Assistant

## Project Overview

CampusCare Mood Assistant is a traditional rule-based chatbot developed using Python and Microsoft Bot Framework. The chatbot is integrated with Azure AI Language Service to analyze the sentiment of user feedback.

The chatbot combines predefined conversation rules with cloud-based Artificial Intelligence. Basic commands are handled using rule-based logic, while Azure AI analyzes the emotional sentiment of user feedback.

---

## Project Objective

The objective of this project is to demonstrate how a traditional chatbot can be integrated with a cloud AI service.

The chatbot can:

- Welcome users.
- Display available commands.
- Analyze user feedback using Azure AI Language Service.
- Identify positive, negative, neutral, or mixed sentiment.
- Handle unsupported input.
- End the conversation politely.

---

## Technologies Used

- Python 3.8
- Microsoft Bot Framework
- Azure AI Language Service
- Azure AI Text Analytics SDK
- Bot Framework Emulator
- Visual Studio Code
- Git and GitHub

---

## Project Structure

```
CampusCareMoodBot/
│
├── app.py
├── config.py
├── bots/
│   └── echo_bot.py
├── requirements.txt
├── README.md
└── deploymentTemplates/
```

---

## How to Run the Project

### Activate the Conda environment

```bash
conda activate campusfind
```

### Install required packages

```bash
pip install -r requirements.txt
pip install azure-ai-textanalytics
```

### Configure Azure environment variables

```bash
export LANGUAGE_KEY="YOUR_AZURE_KEY"
export LANGUAGE_ENDPOINT="YOUR_AZURE_ENDPOINT"
```

### Start the chatbot

```bash
python app.py
```

### Open Bot Framework Emulator

Connect using:

```
http://localhost:3978/api/messages
```

---

## Features

The chatbot supports:

- Greeting users
- Help command
- About command
- Privacy information
- Azure AI sentiment analysis
- Positive sentiment detection
- Negative sentiment detection
- Neutral sentiment detection
- Mixed sentiment detection
- Goodbye message

---

## Example Conversation

```
User: hello

Bot: Hello! Welcome to CampusCare Mood Assistant.

----------------------------------------

User: analyze

Bot: Please type any sentence describing your campus experience.

----------------------------------------

User: The professors are very helpful.

Bot:

Overall Sentiment: Positive

Positive Score: 0.98
Neutral Score: 0.01
Negative Score: 0.01

Thank you for sharing your positive feedback.
```

---

## Security

Azure credentials are stored using environment variables instead of hardcoding them in the source code.

Sensitive information such as API keys should never be committed to GitHub.

---

## Future Improvements

Future versions of the chatbot may include:

- Database integration
- User login
- Feedback history
- Email notifications
- Voice support
- Multiple language support
- Azure OpenAI integration

---

## AI Use Disclosure

Artificial Intelligence was used to assist with understanding Azure AI integration, explaining code, improving documentation, and organizing the report.

The chatbot development, Azure resource creation, coding, testing, screenshots, GitHub repository, and final project submission were completed by the student.

---

## GitHub Repository

Replace this with your repository URL.

```
https://github.com/sarathbontha/CampusCareMoodBot
```

---

## Author

Sarath Bontha

MSAI-631

University of the Cumberlands

Summer 2026