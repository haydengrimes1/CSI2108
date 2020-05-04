#!/bin/python3

import hashlib
import os
import re
from datetime import datetime

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


transactionFile="./file.txt"
directoryName="Blockchain"
lastHashFile="./lastHash.txt"

def clearScreen():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

def makeDirectory():
    try:
        os.mkdir(directoryName)
    except FileExistsError:
        print("Already exists")
    
def makeFirstBlock():
    index="0"
    data="first block"
    timestamp=str(datetime.now())
    previousHash=hashlib.sha256("first block".encode()).hexdigest()
    nonce=calculateNonce(index, data, timestamp, previousHash)
    block=index+"\n"+data+"\n"+timestamp+"\n"+previousHash+"\n"+str(nonce)
    currentHash=hashlib.sha256(block.encode())
    f = open("./" + directoryName + "/" + str(index), "a+")
    f.write(block)
    f.close()
    f2 = open(lastHashFile, "w")
    f2.write(currentHash.hexdigest())
    f2.close()


def checkFirstRun():
    if(os.path.isdir(directoryName)):
        if(os.path.isfile("./"+directoryName+"/0")):
            return
        else:
            makeFirstBlock()
    else:
        makeDirectory()
        makeFirstBlock()

def getLastHash():
    f = open(lastHashFile, "r")
    previousHash = f.readline(256)
    f.close()
    return previousHash

def getCurrentBlockIndex():
    counter=0
    while(os.path.isfile("./"+directoryName+"/"+str(counter))):
        counter=counter+1
    return counter

def createBlock(index, data, timestamp, previousHash):
    nonce=calculateNonce(index, data, timestamp, previousHash)
    block=index+"\n"+data+"\n"+timestamp+previousHash+"\n"+str(nonce)
    currentHash=hashlib.sha256(block.encode())
    f = open("./" + directoryName + "/" + str(index), "a+")
    f.write(block)
    f.close()
    f2 = open(lastHashFile, "w")
    f2.write(currentHash.hexdigest())
    f2.close()

def calculateNonce(index, data, timestamp, previousHash):
    nonce=0
    block=""
    while(nonce != -1):
        block=index+"\n"+data+"\n"+timestamp+"\n"+previousHash+"\n"+str(nonce)
        h = hashlib.sha256(block.encode())
        if(str(h.hexdigest()).count("0") == 14):
            break
        if(nonce == 50000):
            break
        nonce=nonce+1
    return nonce

def main():
    checkFirstRun()
    boolean = True
    while boolean == True:
        try:
            previousHash = getLastHash()
            currentBlockIndex = getCurrentBlockIndex()

            f = open(transactionFile, "r")
            fcontent = f.readlines()
            f.close()
            trans = fcontent[currentBlockIndex-1]
            print("New Transaction Detected...")
            trans = re.sub('{', "", trans)
            trans = re.sub('}', "", trans)
            trans = trans.split(", ")
            sender = trans[0]
            receiver = trans[1]
            amount = trans[2]
            timestamp = trans[3]
            data="{"+sender+", "+receiver+", "+amount+"}"
            createBlock(str(currentBlockIndex), data, timestamp, previousHash)
            boolean=True
            print("Transaction Index '", currentBlockIndex, "' has been accepted into the BlockChain.")

        except IndexError:
            boolean=True
        except FileNotFoundError:
            f = open(transactionFile, "w")
            f.close()
            boolean=True

clearScreen()
print(colour.font.green, "▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆", colour.reset)
print(colour.font.green, "▉                                          ▉", colour.reset)
print(colour.font.green, "▉           ", colour.bold, "Welcome to the", colour.reset, colour.font.green, "            ▉", colour.reset)
print(colour.font.green, "▉            ", colour.bold, "Block Mining", colour.reset, colour.font.green, "             ▉", colour.reset)
print(colour.font.green, "▉              ", colour.bold, "Program", colour.reset, colour.font.green, "                ▉", colour.reset)
print(colour.font.green, "▉                                          ▉", colour.reset)
print(colour.font.green, "▉▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▉", colour.reset)
print("\n")
print("")
print(colour.font.red, "Press 'Ctrl' + 'C' to Exit the Program", colour.reset)
print("\n")
main()