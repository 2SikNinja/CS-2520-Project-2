#Authors: Peter Nguyen
#Assignment: Lab #4
#Completed (or last revision): 10/11/2022
 

# def get_num_of_characters(word):
#    numOfCharacters = 0
#    for char in word:
#        numOfCharacters += 1
#    return numOfCharacters
 
# userInput = input("Please enter the word so I can find out how many characters are in word!: ")
# print("The amount of characters including whitespaces within that word(s) is " + str(get_num_of_characters((userInput))))
 
# def output_without_whitespace(word):
#     numOfCharacters = 0
#     newWords = word.replace(" ","")
#     newWords = newWords.replace('\\t',"")
#     print(newWords)
#     for i in newWords:
#        numOfCharacters += 1
#     return numOfCharacters

# userInput = input("Please enter the word so I can find out how many characters are in word!: ")
# print("The amount of characters including whitespaces within that word(s) is " + str(output_without_whitespace(userInput)))

# def get_acronym(word):
#     acronym = word[0]
#     for i in range(1,len(word)):
#         if word[i-1] == ' ':
#             acronym += word[i]
#     acronym = acronym.upper()
#     return acronym
    

# userInput = input("Please enter the word so I can find out how many characters are in word!: ")
# print(get_acronym(userInput))

# def get_safe(plainText, cipherText):
#     alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#     plainTextList = []
#     keyList = []
#     plainTextWord = plainText.lower()
#     cipherKey = cipherText
#     encryption = ''
    
#     #creates character lists from the inputs
#     for i in plainTextWord:
#         plainTextList.append(i)
#     for j in cipherKey:
#         keyList.append(j)
    
#     #first iterates through the plain text's first letter then onto the alphabet where it goes through each letter then matches it to the keyList or second input from the user
#     for k in range(len(plainTextList)):
#         for o in range(len(alphabet)):
#             if plainTextList[k] == alphabet[o]:
#                 encryption += keyList[o]
#             else:
#                 continue
#     return encryption


# firstInput = input("Input the plain text you would like to encrypt: ")
# cipherText = input("Input the key: ")
# print("The encrypted message is " + get_safe(firstInput, cipherText))


# number = int(input("Enter the amount of prime numbers you'd like: "))
# amount = number
# i,count = 2,0
# primeList = [2]
# k = 2
# while count < amount:
#     if(i<=k / 2):
#         if((k % i) == 0):
#             count+=1
#             primeList.append(k)
#     k+=1
            

# print(primeList)
# def primeGenerator(userInputForPrimes):
#     userInputForPrime = userInputForPrimes
#     bool = False
#     k=2
#     count = 1
#     while(count <= userInputForPrime):
#         if k > 1:
#             for i in range(2, k):
#                 if (k % i) == 0:
#                     bool = True
#                     break
#         if bool:
#             pass
#         else:
#             yield k
#             count+=1
#         bool=False
#         k+=1
        
def prime1000Generator(userInputForPrimes):
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
    # y = int(input("How many prime numbers would you like to generate?: "))
    # x = primeGenerator(y)
    # for i in range(y):
    #     print(str(i+1) + ": " + str(next(x)))
    # z = int(input("How many prime numbers would you like to generate?: "))
    # y = int(input("How many prime numbers would you like to generate?: "))
    x = prime1000Generator(100)
    for i in range(100):
        print(str(i+1) + ": " + str(next(x)))
    y = prime10000Generator(1100)
    for j in range(1101):
        if j == 101 or j == 1100:
            print(str(j) + ": " + str(next(y)))
   
main()