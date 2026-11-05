# -*- coding: utf-8 -*-
"""每天定时通过 QQ 邮箱 SMTP 发送邮件"""
import os
import smtplib
import sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.utils import formataddr

SMTP_SERVER = "smtp.qq.com"
SMTP_PORT = 465  # SSL

sender = os.environ.get("QQ_EMAIL")
auth_code = os.environ.get("QQ_AUTH_CODE")
receiver = os.environ.get("TO_EMAIL")
subject = os.environ.get("MAIL_SUBJECT", "早安 ☀")
content = os.environ.get("MAIL_CONTENT", "早上好，新的一天也要加油哦！")

if not all([sender, auth_code, receiver]):
    print("错误：请先在 GitHub 仓库的 Secrets 中配置 QQ_EMAIL、QQ_AUTH_CODE、TO_EMAIL")
    sys.exit(1)


def main():
    msg = MIMEMultipart()
    msg["From"] = formataddr((str(Header("早安信使", "utf-8")), sender))
    msg["To"] = formataddr((str(Header("朋友", "utf-8")), receiver))
    msg["Subject"] = Header(subject, "utf-8")
    msg.attach(MIMEText(content, "plain", "utf-8"))

    try:
        server = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
        server.login(sender, auth_code)
        server.sendmail(sender, [receiver], msg.as_string())
        server.quit()
        print(f"邮件发送成功：{sender} -> {receiver}")
    except Exception as e:
        print(f"邮件发送失败：{e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
