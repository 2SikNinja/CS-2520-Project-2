#Authors: Peter Nguyen
#Assignment: Lab #4
#Completed (or last revision): 10/11/2022
 
def get_num_of_characters(word):
   numOfCharacters = 0
   for char in word:
       numOfCharacters += 1
   return numOfCharacters
 

def output_without_whitespace(word):
    numOfCharacters = 0
    newWords = word.replace(" ","")
    newWords = newWords.replace('\\t',"")
    for i in newWords:
       numOfCharacters += 1
    return newWords


def get_acronym(word):
    acronym = word[0]
    for i in range(1,len(word)):
        if word[i-1] == ' ':
            acronym += word[i]
    acronym = acronym.upper()
    return acronym
    

def get_safe(plainText, cipherText):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    plainTextList = []
    keyList = []
    plainTextWord = plainText.lower()
    cipherKey = cipherText
    encryption = ''
    
    #creates character lists from the inputs
    for i in plainTextWord:
        plainTextList.append(i)
    for j in cipherKey:
        keyList.append(j)
    
    #first iterates through the plain text's first letter then onto the alphabet where it goes through each letter then matches it to the keyList or second input from the user
    for k in range(len(plainTextList)):
        for o in range(len(alphabet)):
            if plainTextList[k] == alphabet[o]:
                encryption += keyList[o]
            else:
                continue
    return encryption


def main():
    userInput = input("Enter a sentence or phrase: ")
    print("You entered: " + userInput)
    print("Number of characters within the sentence is: " + str(get_num_of_characters(userInput)))
    print("String with no whitespace: " + output_without_whitespace(userInput))
    acronymInput = input("Enter a phrase to generate an acronym: ")
    print("The acronym is: " + get_acronym(acronymInput))
    firstInput = get_acronym(acronymInput)
    cipherText = input("Please enter a 26 long alphabet with no spaces to encrypt your acronym with: ")
    print("Ecrypting " + get_acronym(acronymInput) + " with " + cipherText + " is: " + get_safe(firstInput,cipherText))
    
main()