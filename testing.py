#!/bin/python3

import time
import re
import os
import hashlib
from datetime import datetime

sender=""
receiver=""
amount=""
timestamp=""

fileName="./file.txt"
directoryName="Blockchain"
lastHashFile="./lastHash.txt"

class colour: 
    reset='\033[0m'
    bold='\033[01m'
    disable='\033[02m'
    underline='\033[04m'
    reverse='\033[07m'
    strikethrough='\033[09m'
    invisible='\033[08m'
    class font: 
        black='\033[30m'
        red='\033[31m'
        green='\033[32m'
        orange='\033[33m'
        blue='\033[34m'
        purple='\033[35m'
        cyan='\033[36m'
        lightgrey='\033[37m'
        darkgrey='\033[90m'
        lightred='\033[91m'
        lightgreen='\033[92m'
        yellow='\033[93m'
        lightblue='\033[94m'
        pink='\033[95m'
        lightcyan='\033[96m'
    class bg: 
        black='\033[40m'
        red='\033[41m'
        green='\033[42m'
        orange='\033[43m'
        blue='\033[44m'
        purple='\033[45m'
        cyan='\033[46m'
        lightgrey='\033[47m'



def clearScreen():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

def sleep(x):
    time.sleep(x)

def writeToFile(x):
        f = open(fileName, "a+")
        f.write(x)
        f.close()
        clearScreen()
        print("Data has been Saved.")
        sleep(2)

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
        print(colour.font.yellow + "▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆ " + colour.bold + "  Transaction List" + colour.reset + colour.font.yellow + " ▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆" + colour.reset)
                
        print("")
        print(colour.font.yellow + "There are currently" + colour.bold, transamount, colour.reset + colour.font.yellow + "transactions on file\n\n")
        if(transamount > 0):
            if(transamount > 1):
                print(colour.bold + " <1-" + str(transamount) + ">:          " + colour.reset + colour.font.yellow + "List Inputted Number's Transaction Details")
            else:
                print(colour.bold + " <1>:          " + colour.reset + colour.font.yellow + "List Inputted Number's Transaction Details")
            print(colour.bold + " 'All':          " + colour.reset + colour.font.yellow + "List all Transactions' Details\n")
        print(colour.bold + "'Exit':          " + colour.reset + colour.font.yellow + "Return to the HomeScreen\n")
        selection = input("Enter Selection : " + colour.reset)
        if(selection.lower() == "all"):
            clearScreen()
            print(colour.font.lightcyan + "▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆ " + colour.bold + "  All Transactions" + colour.reset + colour.font.lightcyan + " ▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆" + colour.reset)
                
            print("")
            counter=0
            for trans in transactions:
                counter = counter+1
                trans = re.sub('{', "", trans)
                trans = re.sub('}', "", trans)
                trans = trans.split(", ")
                sender = trans[0]
                receiver = trans[1]
                amount = trans[2]
                timestamp = trans[3]
                print(colour.font.cyan + "▆▆▆▆▆▆▆▆▆▆▆▆ " + colour.bold + "  Transaction #" + str(counter) + colour.reset + colour.font.cyan + " ▆▆▆▆▆▆▆▆▆▆▆▆" + colour.reset)
                print(colour.bold + "Sender:" + colour.reset + colour.font.purple, sender, colour.reset)
                print(colour.bold + "Receiver:" + colour.reset + colour.font.purple, receiver, colour.reset)
                print(colour.bold + "Amount:" + colour.reset + colour.font.purple, amount, colour.reset)
                print(colour.bold + "Timestamp:" + colour.reset + colour.font.purple, timestamp, colour.reset)
                print(colour.font.cyan + "▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆", colour.reset)
                print("")
            input("Press <Enter to Return...>")
        elif(selection.isdigit()):
            if(int(selection) <= transamount):
                number=int(selection)-1
                if(selection == "0"):
                    print(colour.font.red + "\nError: Not a valid input")
                    sleep(1)
                else:
                    clearScreen()
                    try:
                        trans = transactions[number]
                        trans = re.sub('{', "", trans)
                        trans = re.sub('}', "", trans)
                        trans = trans.split(",")
                        sender = trans[0]
                        receiver = trans[1]
                        amount = trans[2]
                        timestamp = trans[3]
                        print(colour.font.cyan + "▆▆▆▆▆▆▆▆▆▆▆▆ " + colour.bold + "  Transaction #" + str(selection) + colour.reset + colour.font.cyan + " ▆▆▆▆▆▆▆▆▆▆▆▆" + colour.reset)
                        print(colour.bold + "Sender:" + colour.reset + colour.font.purple, sender, colour.reset)
                        print(colour.bold + "Receiver:" + colour.reset + colour.font.purple, receiver, colour.reset)
                        print(colour.bold + "Amount:" + colour.reset + colour.font.purple, amount, colour.reset)
                        print(colour.bold + "Timestamp:" + colour.reset + colour.font.purple, timestamp, colour.reset)
                        print(colour.font.cyan + "▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆", colour.reset)
                        print("")
                        input("Press <Enter to Return...>")
                    except IndexError:
                        print(colour.font.red + "\nError: Not a valid input")
                        sleep(1)
            else:
                print(colour.font.red + "\nError: Not a valid input")
                sleep(1)
        elif(selection.lower() == "exit"):
            clearScreen()
        else:
            print(colour.font.red + "\nError: Not a valid input")
            sleep(1)

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
        print(colour.font.cyan + "▆▆▆▆▆▆▆▆▆▆▆▆ " + colour.bold + "  Creating new Transaction" + colour.reset + colour.font.cyan + " ▆▆▆▆▆▆▆▆▆▆▆▆" + colour.reset)        
        print("")
        print(colour.bold + "Transaction Sender:" + colour.reset + colour.font.purple, sender, colour.reset)
        print(colour.bold + "Transaction Receiver:" + colour.reset + colour.font.purple, receiver, colour.reset)
        print(colour.bold + "Transaction Amount:" + colour.reset + colour.font.purple, amount, colour.reset)
                        
        if(sender == ""):
            selection = input(colour.font.purple + "\n\nEnter Transaction Sender (or exit): ")
            sender = selection
            sender = sender.capitalize()
        elif(receiver == ""):
            selection = input(colour.font.purple + "\n\nEnter Transaction Receiver (or exit): ")
            receiver = selection
            receiver = receiver.capitalize()
        elif(amount == ""):
            selection = input(colour.font.purple + "\n\nEnter Transaction Amount (or exit): ")
            if(selection.isdigit()):
                amount = selection
            else:
                print(colour.font.red + "\nError: Not a valid input")
                sleep(1)
        else:
            timestamp = datetime.now()
            clearScreen()
            print(colour.font.cyan + "▆▆▆▆▆▆▆▆▆▆▆▆ " + colour.bold + "  Creating new Transaction" + colour.reset + colour.font.cyan + " ▆▆▆▆▆▆▆▆▆▆▆▆" + colour.reset)        
            print("")
            print(colour.bold + "Transaction Sender:" + colour.reset + colour.font.purple, sender, colour.reset)
            print(colour.bold + "Transaction Receiver:" + colour.reset + colour.font.purple, receiver, colour.reset)
            print(colour.bold + "Transaction Amount:" + colour.reset + colour.font.purple, amount, colour.reset)
            print(colour.bold + "Current Time:" + colour.reset + colour.font.purple, timestamp, colour.reset)
            print(colour.bold + colour.font.green + "\n\n'C': " + colour.reset + colour.font.green + "Confirm Details")
            print(colour.bold + colour.font.red + "'D': " + colour.reset + colour.font.red + "Deny and Re-Enter Details\n")
            print(colour.bold + colour.font.yellow + "'Exit': " + colour.reset + colour.font.yellow + "Return to HomeScreen\n")
            selection = input("Enter Selection: ")
            if(selection.lower() == "c"):
                clearScreen()
                data = "{" + sender + ", " + receiver + ", " + amount + ", " + str(timestamp) + "}\n"
                writeToFile(data)
                selection = "exit"
            elif(selection.lower() == "d"):
                clearScreen()
                sender=""
                receiver=""
                amount=""
                timestamp=""
            elif(selection.lower() == "exit"):
                clearScreen()
            else:
                print(colour.font.red + "\nError: Not a valid input")
                sleep(1)

def analiseBlock():
    selection=""
    while(selection.lower() != "exit"):
        clearScreen()
        counter=0
        while(os.path.isfile("./"+directoryName+"/"+str(counter))):
            counter=counter+1
        clearScreen()
        print(colour.font.yellow + "▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆ " + colour.bold + "  Blockchain Analysis" + colour.reset + colour.font.yellow + " ▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆" + colour.reset)
                
        print("")
        print(colour.font.yellow + "There are currently" + colour.bold, counter, colour.reset + colour.font.yellow + "block in the Blockchain\n\n")
        if(counter-1 > 0):
            print(colour.bold + " <0-" + str(counter-1) + ">:          " + colour.reset + colour.font.yellow + "List Inputted Number's Block Details")
        else:
            print(colour.bold + " <0>:          " + colour.reset + colour.font.yellow + "List Inputted Number's Block Details")
        print(colour.bold + " 'All':          " + colour.reset + colour.font.yellow + "List all Blocks' Details\n")
        print(colour.bold + "'Exit':          " + colour.reset + colour.font.yellow + "Return to the HomeScreen\n")
        selection = input("Enter Selection : " + colour.reset)
        if(selection.lower() == "all"):
            clearScreen()
            counter=0
            while(os.path.isfile("./"+directoryName+"/"+str(counter))):
                f = open("./"+directoryName+"/"+str(counter), "r")
                trans = f.readlines()
                f.close()
                index = trans[0].rstrip('\n')
                data = trans[1].rstrip('\n')
                timestamp = trans[2].rstrip('\n')
                previoushash = trans[3].rstrip('\n')
                nonce = trans[4].rstrip('\n')
                print(colour.font.cyan + "▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆ " + colour.bold + "  Block #" + index + colour.reset + colour.font.cyan + " ▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆" + colour.reset)
                block=index+"\n"+data+"\n"+timestamp+"\n"+previoushash+"\n"+str(nonce)
                currentHash=hashlib.sha256(block.encode())
                print(colour.bold + "BlockHash:" + colour.reset + colour.font.purple, currentHash.hexdigest(), colour.reset)
                print(colour.font.lightcyan + "▆▆" + colour.bold + "  Transaction Data" + colour.reset + colour.font.lightcyan + " ▆▆", colour.reset)
                if("first block" in data):
                    print(colour.bold + "Data:" + colour.reset + colour.font.purple, data, colour.reset)
                else:
                    data2 = re.sub('{', "", data)
                    data2 = re.sub('}', "", data2)
                    data2 = data2.split(", ")
                    print(colour.bold + "Sender:" + colour.reset + colour.font.purple, data2[0], colour.reset)
                    print(colour.bold + "Receiver:" + colour.reset + colour.font.purple, data2[1], colour.reset)
                    print(colour.bold + "Amount:" + colour.reset + colour.font.purple, data2[2], colour.reset)
                
                print(colour.font.lightcyan + "▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆", colour.reset)
                print(colour.bold + "Timestamp:" + colour.reset + colour.font.purple, timestamp, colour.reset)
                print(colour.bold + "Previous Block Hash:" + colour.reset + colour.font.purple, previoushash, colour.reset)
                print(colour.bold + "Nonce:" + colour.reset + colour.font.purple, nonce, colour.reset)

                print(colour.font.cyan + "▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆", colour.reset)
                print("\n")
                counter=counter+1
            input("Press <Enter> to Return...")
        elif(selection.isdigit()):
            if(os.path.isfile("./"+directoryName+"/"+selection)):
                f = open("./"+directoryName+"/"+str(selection), "r")
                trans = f.readlines()
                f.close()
                index = trans[0].rstrip('\n')
                data = trans[1].rstrip('\n')
                timestamp = trans[2].rstrip('\n')
                previoushash = trans[3].rstrip('\n')
                nonce = trans[4].rstrip('\n')
                clearScreen()
                print(colour.font.cyan + "▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆ " + colour.bold + "  Block #" + index + colour.reset + colour.font.cyan + " ▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆" + colour.reset)
                block=index+"\n"+data+"\n"+timestamp+"\n"+previoushash+"\n"+str(nonce)
                currentHash=hashlib.sha256(block.encode())
                print(colour.bold + "BlockHash:" + colour.reset + colour.font.purple, currentHash.hexdigest(), colour.reset)
            
                print(colour.font.lightcyan + "▆▆" + colour.bold + "  Transaction Data" + colour.reset + colour.font.lightcyan + " ▆▆", colour.reset)
                if("first block" in data):
                    print(colour.bold + "Data:" + colour.reset + colour.font.purple, data, colour.reset)
                else:
                    data2 = re.sub('{', "", data)
                    data2 = re.sub('}', "", data2)
                    data2 = data2.split(", ")
                    print(colour.bold + "Sender:" + colour.reset + colour.font.purple, data2[0], colour.reset)
                    print(colour.bold + "Receiver:" + colour.reset + colour.font.purple, data2[1], colour.reset)
                    print(colour.bold + "Amount:" + colour.reset + colour.font.purple, data2[2], colour.reset)
                
                print(colour.font.lightcyan + "▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆", colour.reset)
                print(colour.bold + "Timestamp:" + colour.reset + colour.font.purple, timestamp, colour.reset)
                print(colour.bold + "Previous Block Hash:" + colour.reset + colour.font.purple, previoushash, colour.reset)
                print(colour.bold + "Nonce:" + colour.reset + colour.font.purple, nonce, colour.reset)
                           
                print(colour.font.cyan + "▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆", colour.reset)
                print("")
                input("Press <Enter> to Return...")
                clearScreen()
            else:
                print(colour.font.red + "\nError: Not a valid input")  
                sleep(1)
                clearScreen()
        elif(selection.lower() == "exit"):
            break
        else:
            print(colour.font.red + "\nError: Not a valid input")
            sleep(1)
            clearScreen()
def homeScreen():
    f = open(fileName, "a+")
    f.close()
    selection = "" 
    while selection.lower() != "exit":
        clearScreen()
        print(colour.font.yellow, "▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆", colour.reset)
        print(colour.font.yellow, "▉                                          ▉", colour.reset)
        print(colour.font.yellow, "▉           ", colour.bold, "Welcome to the", colour.reset, colour.font.yellow, "            ▉", colour.reset)
        print(colour.font.yellow, "▉         ", colour.bold, "Transaction Record", colour.reset, colour.font.yellow, "          ▉", colour.reset)
        print(colour.font.yellow, "▉              ", colour.bold, "Program", colour.reset, colour.font.yellow, "                ▉", colour.reset)
        print(colour.font.yellow, "▉                                          ▉", colour.reset)
        print(colour.font.yellow, "▉▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▉")
        print("\n")
        print(colour.bold + "        1: " + colour.reset + colour.font.yellow + "Create a New Transaction")
        print(colour.bold + "        2: " + colour.reset + colour.font.yellow + "View Transactions")
        print(colour.bold + "        3: " + colour.reset + colour.font.yellow + "Analysis Blockchain")
        print("")
        print(colour.bold + "   'Exit': " + colour.reset + colour.font.yellow + "Exit the Program")
        print("\n")
        selection = input("Please Enter a Selection: " + colour.reset)
        if selection == "1":
            newTransaction()
        elif selection == "2":
            listTransactions()
        elif selection == "3":
            analiseBlock()
        elif selection.lower() == "exit":
            clearScreen()
        else:
            print(colour.font.red + "\nError: Not a valid input")
            sleep(1)

    exit

homeScreen()
