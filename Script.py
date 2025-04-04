import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr





# Load recruiter data from local Excel file
# Make sure to change the path to your actual file location
# df = pd.read_excel("F:\DownloadF\Recuriter_Detail.xlsx")  # Make sure this path is correct
df = pd.read_excel("Your data location ")  # Make sure this path is correct

with open("index.html", "r", encoding="utf-8") as file:
    html_template = file.read()
    
    
# Email credentials
your_email = "Your Email"  # Use your Gmail address
# For Gmail, you need to create an App Password if you have 2-Step Verification enabled.
#https://youtu.be/hXiPshHn9Pw?si=kaFtLhKmpkZShf_P
your_app_password = "12 letter Password from your email"  # Use Gmail App Password
resume_link = "Resume Link"

# Start SMTP server
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(your_email, your_app_password)

# Loop through each row and send email

# resume_link = "https://drive.google.com/file/d/1qFf1IJ7YlMwOAzjuXP6UFYhRLY-j1d3_/view?usp=sharing"
# leetcode_link = "https://leetcode.com/u/ankit_3388/"
# codeforces_link = "https://codeforces.com/profile/Ankit3388"
# codechef_link = "https://www.codechef.com/users/ankit3388"
# gfg_link = "https://auth.geeksforgeeks.org/user/err/practice"
# linkedin_link = "https://linkedin.com/in/your-link"
# github_link = "https://github.com/ankit3388"

resume_link="Add resume link"
leetcode_link="Add leetcode link"
codeforces_link="Add codeforces link"
codechef_link="Add codechef link"
gfg_link="Add gfg link"
linkedin_link="Add linkedin link"
github_link="Add github link"



for _, row in df.iterrows():
    print("Excel columns:", df.columns.tolist())

    name = row['Name_Of_Recuriter']
    email = row['Email_Of_Recuriter']
    company = row['Company_Name']
    app_link = row['Application_Link']

    email_body = html_template.format(
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
    msg["Subject"] = f"Referral Request for Opportunity at {company}"

    msg.attach(MIMEText(email_body, "html"))
    try:
        server.sendmail(your_email, email, msg.as_string())
        print(f"Email sent to {name} at {company}")
    except Exception as e:
        print(f"Failed to send to {name}: {e}")

# Quit the server
server.quit()
