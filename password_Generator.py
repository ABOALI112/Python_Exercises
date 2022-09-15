import string as st # Contain the lists of characters, numbers,punctuation
import random as ran  # Contain the shuffle method
    #_summary_ This is a small app that generates password of 8 or more characters.
    #The user supplies the number of characters he wants and the password is generated as he wants
    
list1 = list(st.ascii_letters)      
list2 = list(st.ascii_uppercase)
list3 = list(st.digits)
list4 = list(st.punctuation)

strng = input("How many characters for the password? : ")

while True:
    try:
        strng = int(strng)
        if strng < 8:
           strng = input("Enter 8 or more characters for the password : ")
        else:
            break
    except:
        print("Enter numbers only please ")
        strng = input("How many characters for the password? : ")

ran.shuffle(list1) #shuffle the lists so it is generated randomly
ran.shuffle(list2) 
ran.shuffle(list3)
ran.shuffle(list4)

pass_p1 = round(strng * (50/100))
pass_p3 = round(strng * (50/100))

password = []

for i in range(pass_p1):
    password.append(list1[i])
    password.append(list2[i])

for i in range(pass_p3):
    password.append(list3[i])
    password.append(list4[i])
password="".join(password[0:])

print("your password is: "+ password)