import random

#word list
word_list=["avocado","baboon","camel"]

#randomly selected word from the initial list
chosen_word=random.choice(word_list)
print(((2**6)*'..'))
print("Lets play a guessing game. You guess a letter and we check if it makes up one of the letters in our randomly generated word!\n")
print(f'The randomy generated word is, {chosen_word}\n')

guess="" #created a holding variable for every guessed letter by users

#loop statement to count number of guesses that is equal to chosen random word
for x in chosen_word:

    user_query=input(print("Guess a 'letter' or character making a word: "))
    user_query.lower()
    guess+=user_query
    print(f'You entered, {user_query}. Checking')
    if x==user_query:
        #str()
        print("Letter exist")
        print(f'\nYour made up word is {guess}',end=' ')
    else:
        print("Letter don't exist")
        print(f'\nYour made up word is {guess}',end=' ')




