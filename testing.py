#!/bin/python3

import time
import re
from datetime import datetime

sender=""
receiver=""
amount=""
timestamp=""

fileName="./file.txt"

def clearScreen():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

def sleep(x):
    time.sleep(x)

def writeToFile(x):
    clearScreen()
    selection=input("Save to File (y/n): ")
    if(selection.lower() == "y"):
        f = open(fileName, "a+")
        f.write(x)
        f.close()
        clearScreen()
        print("Data has been Saved.")
        sleep(2)
    else:
        clearScreen()
        print("Data has not been saved to a File.")
        sleep(2)
    

def returnHome():
    clearScreen()
    print("Returning to HomeScreen")
    sleep(0.5)
    clearScreen()
    print("Returning to HomeScreen.")
    sleep(0.5)
    clearScreen()
    print("Returning to HomeScreen..")
    sleep(0.5)
    clearScreen()
    print("Returning to HomeScreen...")
    sleep(0.5)
    clearScreen()

def listTransactions():
    clearScreen()
    f = open(fileName, "r")
    fcontent = f.readlines()
    transamount=0
    transactions = []
    for line in fcontent:
        transamount=transamount+1
        line = re.sub("\n", "", line)
        transactions.append(line)
    f.close()
    selection=""
    while(selection.lower() != "exit"):
        clearScreen()
        print("Transaction List\n")
        print("There are currently", transamount, "transactions on file\n\n")
        print(" <1-" + str(transamount) + ">:          List Inputted Number's Transaction Details")
        print(" 'All':          List all Transactions' Details\n")
        print("'Exit':          Return to the HomeScreen\n")
        selection = input("Enter Selection : ")
        if(selection.lower() == "all"):
            clearScreen()
            print("All Transaction\n")
            counter=0
            for trans in transactions:
                counter = counter+1
                trans = re.sub(",", "", trans)
                trans = re.sub('{', "", trans)
                trans = re.sub('}', "", trans)
                trans = trans.split()
                sender = trans[0]
                receiver = trans[1]
                amount = trans[2]
                timestamp = trans[3] + " " + trans[4]
                print("Transaction #", counter)
                print("Sender: " + sender)
                print("Receiver: " + receiver)
                print("Amount: " + amount)
                print("TimeStamp: " + timestamp)
                print("")
            input("Press <Enter to Return...>")
        elif(selection.isdigit()):
            if(int(selection) <= transamount):
                clearScreen()
                number=int(selection)-1
                trans = transactions[number]
                trans = re.sub(",", "", trans)
                trans = re.sub('{', "", trans)
                trans = re.sub('}', "", trans)
                trans = trans.split()
                sender = trans[0]
                receiver = trans[1]
                amount = trans[2]
                timestamp = trans[3] + " " + trans[4]
                print("Transaction #", number+1)
                print("Sender: " + sender)
                print("Receiver: " + receiver)
                print("Amount: " + amount)
                print("TimeStamp: " + timestamp)
                print("")
                input("Press <Enter to Return...>")
            else:
                clearScreen()
                print("There is not that many transactions")
                sleep(2)
        elif(selection.lower() == "exit"):
            clearScreen()
        else:
            clearScreen()
            print("Not a valid Input")
            sleep(2)
    returnHome()

def newTransaction():
    clearScreen()  
    global sender
    global receiver
    global amount
    global timestamp
    sender = ""
    receiver = ""
    amount = ""
    timestamp = ""
    selection=""

    while(selection.lower() != "exit"):
        clearScreen()
        print("Creating new Transaction\n\n")
        print("Transaction Sender:", sender)
        print("Transaction Receiver:", receiver)
        print("Transaction Amount:", amount)
        if(sender == ""):
            selection = input("\n\nEnter Transaction Sender (or exit): ")
            sender = selection
            sender = sender.capitalize()
        elif(receiver == ""):
            selection = input("\n\nEnter Transaction Receiver (or exit): ")
            receiver = selection
            receiver = receiver.capitalize()
        elif(amount == ""):
            selection = input("\n\nEnter Transaction Amount (or exit): ")
            amount = selection
        else:
            timestamp = datetime.now()
            clearScreen()
            print("Transaction Sender:", sender)
            print("Transaction Receiver:", receiver)
            print("Transaction Amount:", amount)
            print("Current Time: ", timestamp)
            print("\n\n'C': Confirm Details")
            print("'D': Deny and Re-Enter Details\n")
            print("'Exit': Return to HomeScreen\n")
            selection = input("Enter Selection: ")
            if(selection.lower() == "c"):
                clearScreen()
                print("Details Confirmed\n")
                data = "{" + sender + ", " + receiver + ", " + amount + ", " + str(timestamp) + "}\n"
                sleep(1)
                writeToFile(data)
                selection = "exit"
            elif(selection.lower() == "d"):
                clearScreen()
                print("Clearing all Entered Data.")  
                sleep(0.5)
                clearScreen()
                print("Clearing all Entered Data..")  
                sleep(0.5)
                clearScreen()
                print("Clearing all Entered Data..")  
                sleep(0.5)
                sender=""
                receiver=""
                amount=""
                timestamp=""
            elif(selection.lower() == "exit"):
                clearScreen()
            else:
                clearScreen
                print("Invalid Selection")  
                sleep(2)

    returnHome()

def homeScreen():
    selection = 9 
    while selection != "0":
        clearScreen()
        print("Welcome to the Transaction Record Program")
        print("\n\n")
        print("1: Create New Transaction")
        print("2: View Transactions")
        print("")
        print("'exit': Exit the Program\n\n")
        selection = input("Please Enter a Selection: ")
        if selection == "1":
            newTransaction()
        elif selection == "2":
            listTransactions()
        elif selection == "exit":
            clearScreen()
            print("Exiting")
            sleep(0.5)
            clearScreen()
            print("Exiting.")
            sleep(0.5)
            clearScreen()
            print("Exiting..")
            sleep(0.5)
            clearScreen()
            print("Exiting...")
            sleep(0.5)
            clearScreen()
        else:
            print("Unknown")
            sleep(1)

    exit

homeScreen()
