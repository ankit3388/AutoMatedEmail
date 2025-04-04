import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr

import pandas as pd

# Load recruiter data from local Excel file
df = pd.read_excel(r"F:\DownloadF\Recuriter_Detail.xlsx")

# Read both HTML templates
with open("index.html", "r", encoding="utf-8") as f:
    general_template = f.read()

with open("reminder.html", "r", encoding="utf-8") as f:
    reminder_template = f.read()

# Email credentials
your_email = "your_email"
your_app_password = "your_app_password"  # Use App Passwords for Gmail


resume_link="your_resume_link"
leetcode_link="your_leetcode_link"
codeforces_link="your_codeforces_link"
codechef_link="your_codechef_link"
gfg_link="your_gfg_link"
linkedin_link="your_linkedin_link"
github_link="your_github_link"

# SMTP setup
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(your_email, your_app_password)

# Iterate through each row
for _, row in df.iterrows():
    reminder_value = str(row.get('Reminder', '')).strip().lower()

    # Skip if marked as 'done'
    if reminder_value == "done":
        print(f"Skipped: {row['Name_Of_Recuriter']} at {row['Company_Name']} (Marked Done)")
        continue

    is_reminder = reminder_value == "yes"

    # Extract details
    name = row['Name_Of_Recuriter']
    email = row['Email_Of_Recuriter']
    company = row['Company_Name']
    app_link = row['Application_Link']

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

    # Construct and send the email
    msg = MIMEMultipart()
    msg["From"] = formataddr(("Ankit Kumar", your_email))
    msg["To"] = email
    msg["Subject"] = f"Referral Request for Opportunity at {company}"

    msg.attach(MIMEText(email_body, "html"))

    try:
        server.sendmail(your_email, email, msg.as_string())
        print(f"{'Reminder' if is_reminder else 'Email'} sent to {name} at {company}")
    except Exception as e:
        print(f"Failed to send to {name}: {e}")

# Close server
server.quit()
print("All emails processed.")