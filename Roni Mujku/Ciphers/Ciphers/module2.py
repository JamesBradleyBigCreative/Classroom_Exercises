from cryptography.fernet import Fernet
import smtplib

#64 bit encryption

message = "Dr Umar Johnson"

def bitencryption(message):

    global encmessage
    global decmessage
    global key

    # generating a key for encryption
    key = Fernet.generate_key()
    # making function to use generated key
    fernet = Fernet(key)
    # Using key to encrypt message
    encmessage = fernet.encrypt(message.encode())
    # Using key to decrypt
    decmessage = fernet.decrypt(encmessage).decode()

bitencryption(message)

def sendemail(email,encrypted_subject,encrypted_body):
    #connecting to outlook server, email being used
    email_address = "Tradingdevelopment233@outlook.com"
    email_password = "Trading233"
    phone_book = ['']
    
    #opening the connection to the server
    phone_book.append(email)
    with smtplib.SMTP('smtp.office365.com', 587) as smpt:

        smpt.ehlo()
        smpt.starttls()
        # login to email
        smpt.login(email_address, email_password)
        # format and contents of email
        subject = f"Roni {encrypted_subject} "
        body = f" {encrypted_body} "

        msg = f"Subject: {subject}\n\n{body}"
        # sending email
        smpt.sendmail(email_address, phone_book, msg,)

sendemail("roni.mujku@bcestudent.com",key,encmessage)