#Authors: Peter Nguyen
#Assignment: Project #2
#Completed (or last revision): 10/11/2022

import digitprint


def zipCodeReader(zipCode):
    userInput = zipCode
    userInput = userInput.replace('-',"")
    return userInput

def checkSum(zipCode):
    zipCodeList = list(zipCode)
    placeHolder = 0
    for i in zipCodeList:
        placeHolder += int(i)
    checkSum = 10-(placeHolder%10)
    return str(checkSum)


def main():
    userInput = input("Please enter a zip code: ")
    print("The checksum is: " + checkSum(zipCodeReader(userInput)))
    digitprint.digitPrint(zipCodeReader(userInput)+checkSum(zipCodeReader(userInput)))
    
main()