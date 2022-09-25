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

def get_safe(plainText, cipherText):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    plainTextList = []
    keyList = []
    plainTextWord = plainText
    cipherKey = cipherText
    encryption = ''
    l = 0
    for i in plainTextWord:
        plainTextList.append(i)
    for j in cipherKey:
        keyList.append(j)
    print(plainTextList)
    print(keyList)
    for k in range(len(keyList)):
        for o in range(len(plainTextList)):
            if keyList[l] == plainTextList[o]:
                encryption += keyList[l]
            else:
                continue
        l+=1
    return encryption

firstInput = input("Input the plain text you would like to encrypt: ")
cipherText = input("Input the key: ")
print(get_safe(firstInput, cipherText))