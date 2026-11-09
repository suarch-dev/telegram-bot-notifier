# Telegram Disk Alert Bot

A lightweight, on-demand Python script that checks the disk usage on an Apple Silicon MacBook and sends a real-time alert to a Telegram chat if the usage exceeds 80%.

## 🚀 Features
* Uses Python's `subprocess` module to execute native Unix `df` commands.
* Parses system output to extract the exact disk usage percentage.
* Integrates with the Telegram Bot API using `requests`.
* Uses `python-dotenv` to keep API credentials secure.
* Implements `logging` for professional event tracking.

## 🛠️ Tech Stack
* Python 3
* Telegram API
* Subprocess / OS module

## ⚙️ How to Run

1. Clone the repository.
2. Create a virtual environment and install dependencies:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install requests python-dotenv