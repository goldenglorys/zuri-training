# ===================================================================================================
# Improve on your ATM mockup from last course to include the following:

# 1. Use functions

# 2. Include register, and login

# 3. Generate Account Number

# 4. Any other improvement you can think of (extra point)

import datetime
import random

allowedUsers = ["Zenith", "Edward"]
allowedPassword = ["passwordZenith", "passwordEdward"]
accountBalance = 0

database = {}

def init():
    isValidOptionSelected = False
    while isValidOptionSelected == False:
        haveAccount = int(input("Do you have an account with us: 1 (yes) 2 (no) \n"))
        if haveAccount == 1:
            isValidOptionSelected = True
            login()
        elif haveAccount == 2:
            isValidOptionSelected = True
            print(register())
        else:
            print("You have selected an invalid option!")

def withdrawl():
    withdrawlAmount = input("How much would you want to witdrawl?")
    print("Take cash of %s " % withdrawlAmount)

def deposit():
    depositAmount = float(input("How much would you like to deposit?"))
    totalBalance = accountBalance + depositAmount
    print("Total account balance: %s " % totalBalance)

def complaint():
    issue = input("What issue will you like to report? ")
    print("Thank you for contacting us! Our support team would reach out to you soon.")


def generateAccountNumber():
    return random.randint(1111111111, 9999999999)

def register():
    print("========== Account Opening Form =========")
    email = input("Wht is your email? \n")
    fname = input("What is your firstname? \n")
    lname = input("What is your lastname? \n")
    password = input("Create password \n")

    accountNumber = generateAccountNumber()

    database[accountNumber] = {fname, lname, email, password}

    print("Your account has been created.")
    
    login()


def bankOperation():
    print("These are the available options:")
    print("1. Withdrawal")
    print("2. Deposit")
    print("3. Complaint")
    selectedOption = input("Please select an option:")

    if selectedOption == '1':
        withdrawl()
    elif selectedOption == '2':
        deposit()
    elif selectedOption == '3':
        complaint()

def login():
    print("Login to your account")
    name = input("What is your username?\n")
    if name in allowedUsers:
        password = input("What is your password?\n")
        userId = allowedUsers.index(name)
        if password in allowedPassword[userId]:
            print("Welcome %s" % name)
            print("Login date and time is %s" % datetime.datetime.now())
            bankOperation() 
        else:
            print("Password Incorrect, please try again")
    else:
        print("Name not found, please try again")

print("Welcome to Mock bank!")
init()