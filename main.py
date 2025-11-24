import random
import string 
def verify(n):
    a=0
    b=0
    c=0
    l=len(n)
    if l<=8:
        print("try a password more 8 than  characters")
    else:
        for j in range(0,l):
            i=n[j]
            if i.isupper():
                a+=1
            elif i=="@" or i=="_":
                b+=1
            elif i.islower():
                c+=1
            else:
                continue
        if a>0 and b>0 and c>0:
            print("password is strong")
        else:
            if c==0:
                print("use lowercase characters")
            if a==0:
                print("use uppercase characters")
            if b==0:
                        print("use @ or_")
def generator():
    length = int(input("Enter password length: "))
    print('''Choose character set for password from these : 
             1. Digits
             2. Letters
             3. Special characters
             4. Exit''')
    characterList = ""
# Getting character set for password
    while(True):
        choice = int(input("Pick a number "))
        if(choice == 1):       
        # Adding letters to possible characters
            characterList += string.ascii_letters
        elif(choice == 2):        
        # Adding digits to possible characters
            characterList += string.digits
        elif(choice == 3):
        # Adding special characters to possible
        # characters
            characterList += string.punctuation
        elif(choice == 4):
            break
        else:
            print("Please pick a valid option!")
    password = []
    for i in range(length):
    # Picking a random character from our 
    # character list
        randomchar = random.choice(characterList)
    # appending a random character to password
        password.append(randomchar)
# printing password as a string
    print("The random password is " + "".join(password))                  
print("            ","WELCOME TO PASSWORD GENERATOR INTERFACE","            ")
#to ask user if they want a pre-defined or user-defined password
print("For password feedback, input 1")
print("For a predefined password,input 2")
a=int(input("1/2:"))
if a==1:
    b=input("enter your password")
    verify(b)
if a==2:
    generator()
    
