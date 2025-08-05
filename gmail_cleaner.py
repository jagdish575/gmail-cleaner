import imaplib

import os
from dotenv import load_dotenv
load_dotenv()
# Email and app password (enable 2FA and generate app password)
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")  

# Convert comma-separated string to list
UNWANTED_SENDERS = os.getenv("UNWANTED_SENDERS", "").split(",")



def delete_unwanted_emails():
    deleted_count = 0
    try:
        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        mail.login(EMAIL, PASSWORD)
        mail.select("inbox")

        for sender in UNWANTED_SENDERS:
            status, data = mail.search(None, f'FROM "{sender}"')
            if data[0]:
                for num in data[0].split():
                    mail.store(num, "+FLAGS", "\\Deleted")
                    deleted_count += 1
                    print(f"Deleted email #{deleted_count} from {sender}")

        mail.expunge()
        mail.logout()
        print(f" Total deleted: {deleted_count}")
    except Exception as e:
        print(" Error:", e)

    return deleted_count


if __name__ == "__main__":
    delete_unwanted_emails()
