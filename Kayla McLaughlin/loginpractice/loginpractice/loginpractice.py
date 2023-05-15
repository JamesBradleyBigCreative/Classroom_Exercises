import smtplib
import re

name = input("Enter your full name: ")
print("\n")
pattern = "^[A-Za-z]+\ [A-Za-z]"
nameMatch = re.match(pattern, name)
while True:
    if nameMatch:
        print("\n")
        break
    else:
        print("invalid name")
        name = input("Enter your full name: ")
        print("\n")
        pattern = "^[A-Za-z]+\ [A-Za-z]"
        nameMatch = re.match(pattern, name)


dob = input("Please enter your date of birth in the format  dd/mm/yyyy:   ")
print("\n")
pattern = "^[0-9.]+\/[0-9]+\/[0-9]"
dobMatch = re.match(pattern, dob)
while True:
    if dobMatch:
        print("\n")
        break
    else:
        print("invalid date of birth.")
        dob = input("Please enter your date of birth in the format  dd/mm/yyyy:   ")
        print("\n")
        pattern = "^[0-9.]+\/[0-9]+\/[0-9]"
        dobMatch = re.match(pattern, dob)


email = input("Enter your email address: ")

pattern = "^[A-Za-z0-9.]+\@[A-Za-z0-9]+\.[A-Za-z0-9]+$"
mailMatch = re.match(pattern, email)
if mailMatch:
    print("\n")
else:
    print("invalid email.")

print("\n")
username = input("Choose a username:")
print("\n")


password = input("Create a password that is at least 6 characters long: ")
while len(password) <= 5:
    print("\n")
    print ("Password must be at least 6 characters long.")
    password = input("Create a password that is at least 6 characters long: ")



def mail(email,subject,body):
    email_address = "Tradingdevelopment233@outlook.com"
    email_password = "Trading233"
    phone_book = [""]

    phone_book.append(email)
    with smtplib.SMTP("smtp.office365.com",587) as smtp:
        smtp.ehlo()
        smtp.starttls()

        smtp.login(email_address,email_password)
        subject = f'andreas and kayla! {subject}'
        body = f'have fun {body}'

        msg = f'subject: {subject}\n\n{body}'
        smtp.sendmail(email_address,phone_book,msg,)

mail(email,4,5)