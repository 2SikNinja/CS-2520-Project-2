#Authors: Peter Nguyen
#Assignment: Project #2
#Completed (or last revision): 10/11/2022

def digitPrint(zip) :
        printStartStop()
        for i in zip:
                if i == '0':
                        printZero()
                elif i == '1':
                        printOne()
                elif i == '2':
                        printTwo()
                elif i == '3':
                        printThree()
                elif i == '4':
                        printFour()
                elif i == '5':
                        printFive()
                elif i == '6':
                        printSix()
                elif i == '7':
                        printSeven()
                elif i == '8':
                        printEight()
                else:
                        printNine()
        printStartStop()

def printZero():
        zeroBinary = [1, 1, 0, 0, 0]
        for number in zeroBinary:
                if number == 1:
                        print('┃', end='')
                else:
                        print('╻', end='')
                

def printOne():
        oneBinary = [0, 0, 0, 1, 1]
        for number in oneBinary:
                if number == 1:
                        print('┃', end='')
                else:
                        print('╻', end='')

def printTwo():
        twoBinary = [0, 0, 1, 0, 1]
        for number in twoBinary:
                if number == 1:
                        print('┃', end='')
                else:
                        print('╻', end='')

def printThree():
        threeBinary = [0, 0, 1, 1, 0]
        for number in threeBinary:
                if number == 1:
                        print('┃', end='')
                else:
                        print('╻', end='')

def printFour():
        fourBinary = [0, 1, 0, 0, 1]
        for number in fourBinary:
                if number == 1:
                        print('┃', end='')
                else:
                        print('╻', end='')

def printFive():
        fiveBinary = [0, 1, 0, 1, 0]
        for number in fiveBinary:
                if number == 1:
                        print('┃', end='')
                else:
                        print('╻', end='')

def printSix():
        sixBinary = [0, 1, 1, 0, 0]
        for number in sixBinary:
                if number == 1:
                        print('┃', end='')
                else:
                        print('╻', end='')

def printSeven():
        sevenBinary = [1, 0, 0, 0, 1]
        for number in sevenBinary:
                if number == 1:
                        print('┃', end='')
                else:
                        print('╻', end='')

def printEight():
        eightBinary = [1, 0, 0, 1, 0]
        for number in eightBinary:
                if number == 1:
                        print('┃', end='')
                else:
                        print('╻', end='')

def printNine():
        nineBinary = [1, 0, 1, 0, 0]
        for number in nineBinary:
                if number == 1:
                        print('┃', end='')
                else:
                        print('╻', end='')

def printStartStop():
        print('┃', end = '')