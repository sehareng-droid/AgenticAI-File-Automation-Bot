 AgenticAI-File-Automation-Bot

AgenticAI-File-Automation-Bot is a Python tool that allows you to read content from files or folders, summarize it using an AI model, and optionally send the summary via email. It supports multiple file types, logging, and conversation history management.

---

## Features

- Read a single file and get AI-generated summary.
- Process all files in a folder and summarize collectively.
- Send AI-generated summaries via email.
- Maintain conversation history in the session.
- Logging for debugging and error tracking.

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/sehareng-droid/AgenticAI-File-Automation-Bot.git
cd AgenticAI-File-Automation-Bot
Install dependencies:

pip install -r requirements.txt
Create a .env file for API keys or email credentials if needed:

AI_API_KEY=your_api_key_here
EMAIL_USER=your_email_here
EMAIL_PASS=your_email_password_here
Usage
Run the script:

python main.py
The program will prompt you with the following options:

exit → Quit the program

read_file → Read and summarize a single file

process_folder → Read all files in a folder and summarize

send_email → Send the last AI summary via email

history → View the conversation history

clear → Reset the conversation history

save → Save conversation history to a file

Example Workflow
Summarize a single file:

ask anything1: read_file
ask folder path: /path/to/folder
ask file name: sample.txt
AI will read the file, summarize it, and display:

AI Summary:
<summary text here>
Summarize all files in a folder:

ask anything1: process_folder
ask folder path: /path/to/folder
AI will read all files in the folder, combine the content, summarize it, and display:

AI Summary:
<summary text here>
Send the last AI summary via email:

ask anything1: send_email
Enter email: example@example.com
enter subject: AI Summary
Email will be sent with the last AI-generated summary.

View conversation history:

ask anything1: history
Displays all previous files processed and their AI summaries.

Clear conversation history:

ask anything1: clear
Resets the session history.

Save conversation history to a file:

ask anything1: save
Saves all processed files and AI summaries to a text file.

Project Structure
.
├── main.py                # Main program
├── read_content.py        # Reads file content
├── send_ai.py             # Sends content to AI and returns summary
├── send_email.py          # Sends emails
├── logger_config.py       # Logging setup
├── requirements.txt       # Python dependencies
└── README.md              # This file
Dependencies
Python 3.9+

PyPDF2

pandas

smtplib

python-dotenv

logging

Groq (AI client)

Install all dependencies via:

pip install -r requirements.txt
Logging
The application logs errors and important events to help with debugging. Logs are configured via logger_config.py.
