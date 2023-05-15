import pandas as pd
import pwinput
import smtplib 

def encrypt_fibonacci(password):

            ans = ""
            n= 0
            # iterate over the given text
            for i in range(len(password)):
                n = n+i
                ch = password[i]
        
                # check if space is there then simply add space
                if ch==" ":
                    ans+=" "
                # check if a character is uppercase then encrypt it accordingly 
                elif (ch.isupper()):
                    ans += chr((ord(ch) + n-65) % 26 + 65)
                # check if a character is lowercase then encrypt it accordingly
        
                else:
                    ans += chr((ord(ch) + n-97) % 26 + 97)

            return ans

def register():
    # Load existing user data from CSV file
    try:
        df = pd.read_csv("users.csv")
    except FileNotFoundError:
        df = pd.DataFrame(columns=["username", "password", "email"])

    # Prompt user to enter username and password
    while True:
        username = input("Enter a username: ")
        email = input("Enter your email: ")
        password = (pwinput.pwinput(prompt='Enter Password: '))
        confirm_password = pwinput.pwinput(prompt='Confirm Password: ')

        # Check if the username already exists
        if username in df["username"].values:
            print("Username already exists. Please choose another one.")
            

        # Check if the password and confirm_password match
        elif password != confirm_password:
            print("Passwords do not match. Please try again.")
            
        else:
            break
    # Add user data to DataFrame and save to CSV file
    password = encrypt_fibonacci(password)
    df = df.append({"username": username, "password": password,"email": email}, ignore_index=True)
    df.to_csv("users.csv", index=False)

    print("\nRegistration successful!!!")
    sendmail(email,"Your account has been created","Your account has been created")


def login(df):
    username_e = input("To log in please enter your username: ")
    while True:
        if username_e in df["username"].values:
   
            password_e = pwinput.pwinput(prompt='To login please enter your password: ')
            if password_e in df[df["username"]==username_e]["password"].values:
                print("Login Successful !!")
                sendmail(input("Enter Email for confirmation: "),"Account Login Alert","Your account has been entered into, James is balding under his beanie")
                break
            else:
                    print("\nPlease enter a valid password!")
            
def sendmail(email,encrypted_subject,encrypted_body):
    email_address = "Tradingdevelopment233@outlook.com"
    email_password = "Trading233"
    phone_book = [""]
    #connects to outlook servers
    phone_book.append(email)
    with smtplib.SMTP("smtp.office365.com", 587) as smtp:
        smtp.ehlo()
        smtp.starttls()


        smtp.login(email_address,email_password)
        #email structure
        subject = f"Haitham {encrypted_subject}"
        body = f"This is your message {encrypted_body}"


        msg = f"Subject: {subject}\n\n{body}"
        
        smtp.sendmail(email_address,phone_book,msg)


# call the register function


df = pd.read_csv("users.csv")

def intro():
    introduction = input("Hello, would you like to register or login: ")
    introduction = introduction.lower()
    while True:
        if introduction == "register":
            register()
            break
        elif introduction == "login":
            login(df)
            
            break
        else:
            print("\nIncorrect option, please try again! ")

intro()
