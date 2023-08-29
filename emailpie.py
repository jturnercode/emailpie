import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os


def email_noattach(
    subject: str = "", body: str = "", toaddr=os.environ["MAIL_ADDR_DEFAULT"]
):
    """
    Send email within python code.

    Args:
        subject ([str]): [email subject line]
        body (str, optional): [body of email, can be html]. Defaults to "".
        toaddr ([str], optional): [email addresses in string form;
        ex 'j@gmail, k@gmail']. Defaults to env["MAIL_ADDR_DEFAULT"].
    """
    fromaddr: str = os.environ["MAIL_USER"]
    msg = MIMEMultipart()
    # to send multiple recipients toaddr = "a@gmail.com, b@gmail.com"
    msg["From"] = fromaddr
    msg["To"] = toaddr
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "html"))

    server = smtplib.SMTP(os.environ["MAIL_SMTP"], 587)
    server.starttls()
    server.login(fromaddr, os.environ["MAIL_PASS"])
    text = msg.as_string()
    toaddr_lst = toaddr.split(",")
    server.sendmail(fromaddr, toaddr_lst, text)
    server.quit()


def email_attach(
    filepath: str,
    subject: str = "",
    body: str = "",
    toaddr=os.environ["MAIL_ADDR_DEFAULT"],
):
    """
    Send emails within python code.

    Args:
        filepath ([str]): [filename in local dir or fullpath(pref: use '/')]
        subject ([str], optional): [description]
        body ([str], optional): [body of email, can be html]. Defaults to "".
        toaddr ([str], optional): [email addresses in string form;
        ex 'j@gmail, k@gmail']. Defaults to os.environ["MAIL_ADDR_DEFAULT"].
    """
    fromaddr = os.environ["MAIL_USER"]
    msg = MIMEMultipart()
    msg["From"] = fromaddr
    # to send multiple recipients toaddr = "a@gmail.com, b@gmail.com"
    msg["To"] = toaddr
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "html"))

    # filepath can be filename only for local directory files
    # otherwise should be the entire or relative path with filename
    attachment = open(filepath, "rb")

    part = MIMEBase("application", "octet-sream")
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    _, filename = os.path.split(filepath)
    part.add_header("Content-Disposition", "attachment; filename = %s" % filename)

    msg.attach(part)

    server = smtplib.SMTP(os.environ["MAIL_SMTP"], 587)
    server.starttls()
    server.login(fromaddr, os.environ["MAIL_PASS"])
    text = msg.as_string()
    toaddr_lst = toaddr.split(",")
    server.sendmail(fromaddr, toaddr_lst, text)
    server.quit()
