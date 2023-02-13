# this is crazy bank

import random
print("Welcome to Crazy Bank")
print("Select the choice")
print("Are you an exisiting user? Enter 1")
print("Are you a new user? Enter 2")
choice=int(input("Enter the number 1 or 2"))
if choice==1:
    print("You are an Existing User")
    #it should be of 10 digits number
    Account_Number=(int(input("Enter your Bank Account Number")))
else:
    print("You are a New User")
    First_Name=input("Enter your First Name")
    Last_Name=input("Enter your Last Name")
    print(" Welcome"+First_name +Last_Name)
    print(" Our Bank offers to open 4 types of account")
    print("1. Chequing Account")
    print("2. Saving Account")
    print("3. Student Account")
    print("4. Senior Bank Account")
    choice_for_bank_account=int(input("Enter the type of Bank Account you want to open"))
    if choice_for_bank_account==1:
        print (" Chequing Account")
        CANo=random.randint(1000000000,9999999999)#the computer will generate the 10 digit number automatically.
        print(" Your account number for the chequing account is"+CANo)
    
    
    
    
    
    
