import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr

# Load recruiter data from local Excel file
df = pd.read_excel(r"F:\DownloadF\Recuriter_Detail.xlsx")  # Use raw string

# Read both HTML templates
with open("index.html", "r", encoding="utf-8") as f:
    general_template = f.read()

with open("reminder.html", "r", encoding="utf-8") as f:
    reminder_template = f.read()

# Email credentials
your_email = "Your mail address"  # Use your actual email address
# Note: Use your actual email address
# App password for Gmail (if using 2FA)
your_app_password = "your_app_password"  # Use your actual app password
# Note: Make sure to use an app password if you have 2FA enabled on your Gmail account.

# Shared links
# resume_link = "https://drive.google.com/file/d/1qFf1IJ7YlMwOAzjuXP6UFYhRLY-j1d3_/view?usp=sharing"
# leetcode_link = "https://leetcode.com/u/ankit_3388/"
# codeforces_link = "https://codeforces.com/profile/Ankit3388"
# codechef_link = "https://www.codechef.com/users/ankit3388"
# gfg_link = "https://auth.geeksforgeeks.org/user/err/practice"
# linkedin_link = "https://linkedin.com/in/your-link"
# github_link = "https://github.com/ankit3388"



resume_link="Your resume link"
leetcode_link="Your leetcode link"
codeforces_link="Your codeforces link"
codechef_link="Your codechef link"
gfg_link="Your gfg link"
linkedin_link="Your linkedin link"
github_link="Your github link"

# SMTP setup
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(your_email, your_app_password)

# Iterate through each row
for _, row in df.iterrows():
    name = row['Name_Of_Recuriter']
    email = row['Email_Of_Recuriter']
    company = row['Company_Name']
    app_link = row['Application_Link']
    is_reminder = str(row.get('Reminder', '')).strip().lower() == "yes"

    # Choose correct template
    selected_template = reminder_template if is_reminder else general_template

    # Format the email body
    email_body = selected_template.format(
        name=name,
        company=company,
        app_link=app_link,
        resume_link=resume_link,
        leetcode_link=leetcode_link,
        codeforces_link=codeforces_link,
        codechef_link=codechef_link,
        gfg_link=gfg_link,
        linkedin_link=linkedin_link,
        github_link=github_link
    )

    msg = MIMEMultipart()
    msg["From"] = formataddr(("Ankit Kumar", your_email))
    msg["To"] = email
    msg["Subject"] = f"Referral Request for Opportunity at {company}"  # even for reminder
    msg.attach(MIMEText(email_body, "html"))

    try:
        server.sendmail(your_email, email, msg.as_string())
        print(f"{'Reminder' if is_reminder else 'Email'} sent to {name} at {company}")
    except Exception as e:
        print(f"Failed to send to {name}: {e}")

server.quit()
