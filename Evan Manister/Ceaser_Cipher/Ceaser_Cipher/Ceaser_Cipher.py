from email.message import EmailMessage
import smtplib

email = input("Enter your email: ")
message = input("Enter a message: ")



def encrypt_text(plaintext,n):
        #Defining the encrypt text
    ans = ""
        # Iterate over the given text
    for i in range(len(plaintext)):
        ch = plaintext[i]
        # check if space is there then simply add space 
        if ch==" ":
            ans+=" "
        # check of a character is upercase then encrypt it accordingly
        elif (ch.isupper()):
            ans += chr((ord(ch) + n-65) % 26 + 65)
        # check if a character is lowercase then encrypt it accordingly

        else:
            ans += chr((ord(ch) + n-97) % 26 + 97)

    return ans

def encrypt_text(plaintext):
        #Defining the encrypt text
    ans = ""
    n = 0
        # Iterate over the given text
    for i in range(len(plaintext)):
        ch = plaintext[i]
        n=n+i
        # check if space is there then simply add space 
        if ch==" ":
            ans+=" "
        # check of a character is upercase then encrypt it accordingly
        elif (ch.isupper()):
            ans += chr((ord(ch) + n-65) % 26 + 65)
        # check if a character is lowercase then encrypt it accordingly

        else:
            ans += chr((ord(ch) + n-97) % 26 + 97)

    return ans

def decrypt_text(plaintext):
        #Defining the encrypt text
    ans = ""
    n=0
        # Iterate over the given text
    for i in range(len(plaintext)):
        n= n+i
        ch = plaintext[i]
        # check if space is there then simply add space 
        if ch==" ":
            ans+=" "
        # check of a character is upercase then encrypt it accordingly
        elif (ch.isupper()):
            ans += chr((ord(ch) - n-65) % 26 + 65)
        # check if a character is lowercase then encrypt it accordingly

        else:
            ans += chr((ord(ch) - n-97) % 26 + 97)

def decrypt_text(plaintext,n):
        #Defining the encrypt text
    ans = ""
        # Iterate over the given text
    for i in range(len(plaintext)):
        ch = plaintext[i]

        # check if space is there then simply add space 
        if ch==" ":
            ans+=" "
        # check of a character is upercase then encrypt it accordingly
        elif (ch.isupper()):
            ans += chr((ord(ch) - n-65) % 26 + 65)
        # check if a character is lowercase then encrypt it accordingly

        else:
            ans += chr((ord(ch) - n-97) % 26 + 97)

    return ans

def sendmail(email, encrypted_subject, encrypted_body):
    email_adress = 'Tradingdevelopment233@outlook.com'
    # This is the email you will be using to send the message with
    email_password = 'Trading233'
    # This is the password you will have to use to use the email adress
    phone_book = ['']

    phone_book.append(email)
    with smtplib.SMTP('smtp.office365.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()

        smtp.login(email_adress, email_password)

        subject = f'evan {encrypted_subject}'
        # Name of the email subject
        body = f'{encrypted_body}'

        msg = f'Subject: {subject}\n\n{body}'
        # Message inside the email
        smtp.sendmail(email_adress, phone_book, msg,)

 


plaintext = "IFMMP FWFSZPOF"
# Text inside the message
n = 1 
encm = encrypt_text(plaintext)
plaintext = decrypt_text(plaintext, n)
print(plaintext)
# Print the text inside the message

#print ("Plain Text is : " + plaintext)
#print ("Shift pattern is: " + str(n))
#print ("Cipher Text is : " + encrypt_text(plaintext,n))

sendmail(email,n,encm)






