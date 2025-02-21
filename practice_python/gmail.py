from email.message import EmailMessage
import smtplib
from dotenv import load_dotenv
import os


load_dotenv()
GMAIL =os.getenv("GMAIL")
GMAIL_PASSWORD = os.getenv("GMAIL_PASSWORD")

# setting
msg=EmailMessage()
msg["From"]=GMAIL
msg["To"]="amy19951018@gmail.com"
msg["Subject"]="你好你好"

# content
msg.set_content("測試看看ver02")
msg.add_alternative("<h1>這是一封 HTML 郵件！</h1>", subtype="html")
# # 加入附件（假設有 test.pdf）
# with open("test.pdf", "rb") as f:
#     msg.add_attachment(f.read(), maintype="application", subtype="pdf", filename="test.pdf")


# 連線到 SMTP Sever，可以在網路上找到 smtp sever
# sever=smtplib.SMTP_SSL("smtp.gmail.com", 465)
# sever.login(GMAIL, GMAIL_PASSWORD)
# sever.send_message(msg)
# sever.close()

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(GMAIL, GMAIL_PASSWORD)
    server.send_message(msg)

print("郵件發送成功！🎉")
