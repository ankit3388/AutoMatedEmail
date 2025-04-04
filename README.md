# AutoMatedEmail

This is a Python-based automated email script that sends **customized job referral requests** or **follow-up reminders** to recruiters using Gmail. The recruiter details and job links are stored in an Excel sheet, and emails are sent using an HTML template.

---

## ✨ Features

- Automatically sends personalized **referral request emails** to recruiters.
- Sends **gentle reminder emails** if specified in the Excel file.
- **Skips** sending emails if marked as `done` in the Reminder column.
- Reads recruiter details from an Excel spreadsheet.
- Uses **Gmail SMTP** for email delivery.
- Includes clickable links to Resume, LinkedIn, GitHub, and coding profiles.
- Uses elegant **HTML templates** for formatting.

---

## Folder Structure

AutoMatedEmail/ │ ├── index.html # Email template for initial referral message ├── reminder.html # Email template for gentle reminder follow-up ├── Script.py # Main Python script ├── Recuriter_Detail.xlsx # Excel file with recruiter information └── README.md # Documentation


---

## Setup Instructions

### 1. Requirements

- Python 3.7+
- `pandas`
- An active Gmail account
- An App Password (for Gmail)

### 2. Install Required Libraries

```bash
pip install pandas openpyxl
```
### 3. Enable Gmail App Password
- If 2-Step Verification is enabled, create an App Password for your Gmail:
```
Steps:
Go to Google App Passwords
Select "Mail" and "Windows Computer"
Generate & copy the password (e.g. abcd efgh ijkl mnop)
Replace the your_email and your_app_password variables in the script with your own Gmail credentials.
```

📄 Excel Format (Recuriter_Detail.xlsx)
Your Excel file must have the following columns:
```
Name_Of_Recuriter	   Email_Of_Recuriter	Company_Name	    Application_Link	    Reminder
John Doe	             john@example.com	      Google	         https://link	      No
Jane Smith	          jane@example.com	      Amazon	         https://link	      Yes
```

- If Reminder = Yes, the script sends a follow-up using reminder.html.
- If Reminder = No, it sends the initial mail using index.html.
- If Reminder = Done, No email is sent

📜 How to Use
```
Step 1: Customize Templates
Edit index.html and reminder.html with your personal branding, message, and signature.

Step 2: Edit Python Script
Open Script.py and configure the following:

your_email = "youremail@gmail.com"
your_app_password = "your_app_password"
resume_link = "https://your_resume_link"
Replace coding profile & LinkedIn links with your own.

Step 3: Run the Script
python send_email.py
The script will:

Read all entries from the Excel file.

Format the email based on Reminder column.

Send the email to each recruiter with personalized content.
```

### 4 Customization
You can modify:
- Email subject line
- HTML formatting
- Add attachments

Use different email providers (like Outlook, Yahoo) by changing SMTP config
