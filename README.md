# 📬 Gmail Auto Email Cleaner

This Python script automatically deletes unwanted emails from your Gmail inbox using the IMAP protocol. It is designed to clean up spammy or irrelevant emails from specific senders by using a secure `.env` configuration.

---

## ✨ Features

- Deletes emails from specific senders (you define them)
- Uses IMAP over SSL for secure access
- Loads email credentials and sender list from `.env` file
- Lightweight, no database required
- Clean and safe: no inbox-wide deletion

---

## 📁 Project Structure

.
├── delete_emails.py # Main script
├── .env # Store your email, password, sender list
├── .gitignore # Prevents uploading .env
├── README.md # You're reading it
└── requirements.txt # python-dotenv only


---

## ⚙️ Setup Instructions

### 1. Clone the Repository


git clone https://github.com/pydataindore/pydata-indore.git
cd pydata-indore
2. Create and Activate Virtual Environment

python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
3. Install Required Packages
pip install -r requirements.txt

4. Create a .env File
EMAIL=your-email@gmail.com
PASSWORD=your-app-password
UNWANTED_SENDERS=jobalerts-noreply@linkedin.com,do-not-reply@indeed.com,...
💡 You can add as many senders as needed, separated by commas.

▶️ How to Run
python delete_emails.py
The script will:

Log into your Gmail via IMAP

Search for emails from the unwanted senders

Mark them for deletion

Expunge (permanently delete) them

🔐 Important Security Note
Use App Passwords if you have 2-Step Verification enabled on Gmail.

Never commit your .env file.

.env is already included in .gitignore for safety.

📦 Requirements
Python 3.x

python-dotenv (for managing environment variables)

📄 License
This project is open-source and free to use under the MIT License.