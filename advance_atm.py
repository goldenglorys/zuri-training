import datetime
import random

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
            init()

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

def transferWithin():
    from_account = int(input("Enter account number to trasfer from: \n"))
    to_account = int(input("Enter account number to transfer to: \n"))
    amount = int(input("Enter amount: \n"))
    description = input("Description: \n")
    for accountNumber, userDetails in database.items():
        print(accountNumber)
        if accountNumber == from_account:
            print("%s on it way to %s." % (amount, to_account))
        else:
            print("Invalid account number, please try again")
            transferWithin()

def register():
    print("========== Account Opening Form =========")
    email = input("Wht is your email? \n")
    fname = input("What is your firstname? \n")
    lname = input("What is your lastname? \n")
    password = input("Create password \n")

    accountNumber = generateAccountNumber()

    database[accountNumber] =  [ fname, lname, email, password ]

    print("Your account has been created. %s" % accountNumber)
    
    login()


def bankOperation(user):
    print("Welcome %s %s. These are the available options:" % ( user[0],  user[1] ))
    print("1. Withdrawal")
    print("2. Deposit")
    print("3. Same bank trasfer")
    print("4. Complaint")
    selectedOption = input("Please select an option:")

    if selectedOption == '1':
        withdrawl()
    elif selectedOption == '2':
        deposit()
    elif selectedOption == '3':
        transferWithin()
    elif selectedOption == '4':
        complaint()
    else:
        print("Invalid option selected")
        bankOperation(user)

def login():
    print("============== Login to your account ===============")
    isLoginSuccessful = False
    while isLoginSuccessful == False:
        accountNumberFromuser = int(input("What is your account number? \n"))
        password = input("What is your password?  \n")
        for accountNumber, userDetails in database.items():
            if accountNumber == accountNumberFromuser:
                if userDetails[3] == password:
                            isLoginSuccessful = True
        print("Invalid account or passowrd")
    bankOperation(userDetails)

print("Welcome to Mock bank!")
init()