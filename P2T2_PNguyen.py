#Authors: Peter Nguyen
#Assignment: Lab #4
#Completed (or last revision): 10/11/2022

import time
import turtle

def primeGenerator(userInputForPrimes):
    userInputForPrime = userInputForPrimes
    bool = False
    k=2
    count = 1
    while(count <= userInputForPrime):
        if k > 1:
            for i in range(2, k):
                if (k % i) == 0:
                    bool = True
                    break
        if bool:
            pass
        else:
            yield k
            count+=1
        bool=False
        k+=1
        
def prime10000Generator(userInputForPrimes):
    userInputForPrime = userInputForPrimes
    bool = False
    k=2
    count = 1
    while(count <= userInputForPrime):
        if k > 1:
            for i in range(2, k):
                if (k % i) == 0:
                    bool = True
                    break
        if bool:
            pass
        else:
            if(count == 101 or count == 1100):
                yield k
            count+=1
        bool=False
        k+=1

def main():
    x = primeGenerator(100)
    for i in range(100):
        print(str(i+1) + ": " + str(next(x)))
    y = prime10000Generator(1100)
    for j in range(1101):
        if j == 101 or j == 1100:
            print(str(j) + ": " + str(next(y)))
startTime = time.time()
main()
finalTime = (time.time() - startTime)
print("Execution time is = " + str(finalTime) + " seconds")