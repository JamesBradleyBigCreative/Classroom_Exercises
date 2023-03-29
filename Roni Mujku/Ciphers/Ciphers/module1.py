def vig_encrypt_text(plaintext):
    ans = ""

    # Generating a list containing fibonacci sequence until length of text
    n1, n2 = 0, 1
    count = 0
    list1 = [n1,n2]
    while count < len(plaintext):
       if plaintext[count] == " ":
           count += 1
           continue
       #print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       list1.append(nth)
       count += 1
    #print(list1)

    # iterate over the given text
    for i in range(len(plaintext)):
        ch = plaintext[i]
        #print(list1[i])
        # check if a character is uppercase then encrypt it accordingly
        # modulo allows for wrapping around the alphabet
        if (ch.isupper()):
            ans += chr((ord(ch) + list1[i]-65) % 26 + 65)
        # check if a character is lowercase then encrypt it accordingly
        
        elif (ch.islower()):
            ans += chr((ord(ch) + list1[i]-97) % 26 + 97)

        else:
            ans += ch
    
    return ans

def vig_decrypt_text(plaintext):
    ans = ""

    # Generating a list containing fibonacci sequence until length of text
    n1, n2 = 0, 1
    count = 0
    list1 = [n1,n2]
    while count < len(plaintext):
       if plaintext[count] == " ":
           count += 1
           continue
       #print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       list1.append(nth)
       count += 1

    for i in range(len(plaintext)):
        ch = plaintext[i]
        if (ch.isupper()):
            ans += chr((ord(ch) - list1[i]-65) % 26 + 65)
        # check if a character is lowercase then encrypt it accordingly
        
        elif (ch.islower()):
            ans += chr((ord(ch) - list1[i]-97) % 26 + 97)

        else:
            ans += ch

    return ans

x = vig_encrypt_text("https://i.redd.it/vzgvm9l5ejh91.jpg")

vig_decrypt_text(x)
