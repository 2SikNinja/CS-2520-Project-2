#Authors: Peter Nguyen
#Assignment: Lab #4
#Completed (or last revision): 10/11/2022


#Task 1 
def get_num_of_characters(word):
   numOfCharacters = 0
   for char in word:
       numOfCharacters += 1
   return numOfCharacters
 
#Task 2
def output_without_whitespace(word):
    numOfCharacters = 0
    newWords = word.replace(" ","")
    newWords = newWords.replace('\\t',"")
    for i in newWords:
       numOfCharacters += 1
    return newWords

#Task 3
def get_acronym(word):
    acronym = word[0]
    for i in range(1,len(word)):
        if word[i-1] == ' ':
            acronym += word[i]
    acronym = acronym.upper()
    return acronym
    
#Task 4
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

#Task 5
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


#Task 6   
main()


# Output
# Enter a sentence or phrase: The only thing we have to fear is fear itself
# You entered: The only thing we have to fear is fear itself
# Number of characters within the sentence is: 45
# String with no whitespace: Theonlythingwehavetofearisfearitself
# Enter a phrase to generate an acronym: random access memory
# The acronym is: RAM
# Please enter a 26 long alphabet with no spaces to encrypt your acronym with: bpzhgocvjdqswkimlutneryaxf 
# Ecrypting RAM with bpzhgocvjdqswkimlutneryaxf is: ubw

# Enter a sentence or phrase: Hey I'm Peter
# You entered: Hey I'm Peter
# Number of characters within the sentence is: 13
# String with no whitespace: HeyI'mPeter
# Enter a phrase to generate an acronym: I got to Cal Poly Pomona
# The acronym is: IGTCPP
# Please enter a 26 long alphabet with no spaces to encrypt your acronym with: bpzhgocvjdqswkimlutneryaxf
# Ecrypting IGTCPP with bpzhgocvjdqswkimlutneryaxf is: jcnzmm

# Enter a sentence or phrase: I take CS2560 with Professor Yang
# You entered: I take CS2560 with Professor Yang
# Number of characters within the sentence is: 33
# String with no whitespace: ItakeCS2560withProfessorYang
# Enter a phrase to generate an acronym: I love this class
# The acronym is: ILTC
# Please enter a 26 long alphabet with no spaces to encrypt your acronym with: bpzhgocvjdqswkimlutneryaxf
# Ecrypting ILTC with bpzhgocvjdqswkimlutneryaxf is: jsnz