correct_Username = 'person.jpeg'
correct_Password = 'password123'

user_name = None
user_password = None
attempts = 0
while user_name != correct_Username and user_password != correct_Password:
    
    attempts += 1
    if attempts == 1:
        user_name = str(input('Enter username: '))
        user_password = str(input('Enter password: '))

    if user_name != correct_Username or user_password != correct_Password:
        print('Wrong username or password please try again')
        user_name = str(input('Enter username: '))
        user_password = str(input('Enter password: '))
    elif user_name == correct_Username and user_password == correct_Password:
        print('Access granted')
    
    if attempts == 3 and user_name != correct_Username and user_password != correct_Password:
        print('Access denied')
        break