import smtplib
import module1
from cryptography.fernet import Fernet

def encrypt_text(plaintext,n):
    ans = ""
    # iterate over the given text
    for i in range(len(plaintext)):
        ch = plaintext[i]

        # check if a character is uppercase then encrypt it accordingly
        # modulo allows for wrapping around the alphabet
        if (ch.isupper()):
            ans += chr((ord(ch) + n-65) % 26 + 65)
        # check if a character is lowercase then encrypt it accordingly
        
        elif (ch.islower()):
            ans += chr((ord(ch) + n-97) % 26 + 97)

        else:
            ans+= ch
    
    return ans

def decrypt(encrypted_message,k):
    #encrypted message(string) parameter
    #k key value to decrypt
    encrypted_message = encrypted_message.strip()
    
    letters="abcdefghijklmnopqrstuvwxyz"
    
    decrypted_message = ""

    # loop through message, compare each character to stored letters
    # shift character by key to the left
    for ch in encrypted_message:

        if ch in letters:
            position = letters.find(ch)
            new_pos = (position - k) % 26
            new_char = letters[new_pos]
            decrypted_message += new_char

        elif ch in letters.upper():
            position = letters.upper().find(ch)
            new_pos = (position - k) % 26
            new_char = letters.upper()[new_pos]
            decrypted_message += new_char

        else:
            decrypted_message += ch

    print("Your decrypted message is:\n")
    print(decrypted_message)
    return decrypted_message

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

def startup():
    print("""
    ______________    ______________
    |Encrypt('E')|    |Decrypt('D')|
    --------------    --------------
               ____________
               |Email('S')|
               ------------
    """)
    x = input("Do you want to encrypt or decrypt or send an encrypted email(E/D/S): ")
    x = x.upper()

    if x == 'E':
        print("""
        _____________    _______________
        |Ceaser('C')|    |Vigenere('V')|
        -------------    ---------------
        """)

        y = input("\nDo you want to use ceaser cipher or vigenere cypher (V/C): ")
        y = y.upper()

        if y == 'C':
            plaintext = input("\nEnter plain text to encrypt: ")
            n = 4
            answer = encrypt_text(plaintext,n)
            print("Plain Text is : " + plaintext)
            print("Shift pattern is : " + str(n))
            print("Cipher Text is : " + answer)

            # Putting cypher text in a text file
            f = open("test.txt","w")
            f.write(answer)
            f.close()

            return answer

        elif y == 'V':
            plaintext = input("\nEnter plain text to encrypt: ")
            answer = module1.vig_encrypt_text(plaintext)
            print(answer)

            f = open("test.txt","w")
            f.write(answer)
            f.close()

            return answer

    elif x == 'D':
        cipher = input("\nEnter message to decrypt: ")
        try:
            key = int(input("Enter key value for decryption:"))
        except:
            print("ERROR")
            quit()
        answer = decrypt(cipher,key)
        # Putting decrypted text in a text file
        f = open("test.txt","w")
        f.write(answer)
        f.close()

        return answer

    elif x == 'S':
        answer = input("\nEnter encrypted message")
        shift = 4
        #print("Main " + answer)
        emailinput = input("Enter your Email: ")
        sendemail(emailinput,shift,answer)

    else:
        print("ERROR")
        quit()

#answer = startup()
#answer = module1.vig_encrypt_text(
#    "https://i.redd.it/vzgvm9l5ejh91.jpg")
#shift = 4
##print("Main " + answer)
#emailinput = input("Enter your Email: ")

#sendemail(emailinput,shift,answer)

startup()