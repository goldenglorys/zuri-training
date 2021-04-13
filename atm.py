# ===================================================================================================
# Improve on your ATM mockup from last course to include the following:

# 1. Use functions

# 2. Include register, and login

# 3. Generate Account Number

# 4. Any other improvement you can think of (extra point)

import datetime

name = input("What is your username?\n")

allowedUsers = ["Zenith", "Edward"]
allowedPassword = ["passwordZenith", "passwordEdward"]
accountBalance = 0

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

def loginInfo():
    print("Welcome %s" % name)
    print("Login date and time is %s" % datetime.datetime.now())
    print("These are the available options:")
    print("1. Withdrawal")
    print("2. Deposit")
    print("3. Complaint")
    
if name in allowedUsers:
    password = input("What is your password?\n")
    userId = allowedUsers.index(name)
    if password in allowedPassword[userId]:
        loginInfo()

        selectedOption = input("Please select an option:")

        if selectedOption == '1':
            withdrawl()
        elif selectedOption == '2':
            deposit()
        elif selectedOption == '3':
           complaint()
             
    else:
        print("Password Incorrect, please try again")
else:
    print("Name not found, please try again")