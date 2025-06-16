# 📬 Automated Email Report

This Python script reads a CSV file of weekly team commits and sends it out as an email using Gmail’s SMTP.

### What it does

- Reads commit data from a `.csv` file
- Adds the content to the email body
- Attaches the CSV file to the email
- Uses environment variables for email info and credentials

---

### Setup

1. Clone the repo
2. Create a .env file (see .env.example) with:

```env
COMMIT_FILE=path/to/your/commits.csv
FROM=your.email@gmail.com
TO=recipient.email@example.com
PASSWORD=your_app_password
```

3.Install dependencies: pip install -r requirements.txt

4.Run the script: python automated-email-report.py

### Notes

If using Gmail with 2FA, you’ll need to generate an App Password.
Make sure “Less secure app access” is enabled if you're not using App Passwords (not recommended).
SMTP server: smtp.gmail.com on port 587 with STARTTLS
