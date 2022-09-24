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