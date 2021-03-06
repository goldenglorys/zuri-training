import datetime

name = input("What is your username?\n")

allowedUsers = ["Zenith", "Edward"]
allowedPassword = ["passwordZenith", "passwordEdward"]
accountBalance = 0

if name in allowedUsers:
    password = input("What is your password?\n")
    userId = allowedUsers.index(name)
    if password in allowedPassword[userId]:
        print("Welcome %s" % name)
        print("Login date and time is %s" % datetime.datetime.now())
        print("These are the available options:")
        print("1. Withdrawal")
        print("2. Deposit")
        print("3. Complaint")

        selectedOption = input("Please select an option:")

        if selectedOption == '1':
            withdrawlAmount = input("How much would you want to witdrawl?")
            print("Take cash of %s " % withdrawlAmount)
        elif selectedOption == '2':
            depositAmount = float(input("How much would you like to deposit?"))
            totalBalance = accountBalance + depositAmount
            print("Total account balance: %s " % totalBalance)
        elif selectedOption == '3':
            issue = input("What issue will you like to report? ")
            print("Thank you for contacting us! Our support team would reach out to you soon.")
             
    else:
        print("Password Incorrect, please try again")
else:
    print("Name not found, please try again")