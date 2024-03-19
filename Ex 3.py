import random

#word list
word_list=["avocado","baboon","camel"]

#randomly selected word from the initial list

print(((2**6)*'..'))
print("Lets play a guessing game. You guess a letter and we check if it makes up one of the letters in our randomly generated word!\n")
chosen_word=random.choice(word_list)
word_length=len(chosen_word)

print(f'The randomy generated word is, {chosen_word}\n')

#creating blanks for every randomly selected word
display=[]

for x in range(word_length):
    display.append('-')

guess="" #created a holding variable for every guessed letter by users

#loop statement to count number of guesses that is equal to chosen random word
for y in range(word_length):
    holding_letter=chosen_word[y]
    print(display)
    user_query=input(print(f"\n Guess a 'letter' or character making a word. You have {len(display)} guesses"))
    user_query.lower()
    guess+=user_query
    print(f'You entered, {user_query}. Checking')
    if holding_letter==user_query:
        display[y]=holding_letter
        #str()
        print("Letter exist")
        display.insert(x,user_query)
        print(f'\nYour made up word is {guess}',end=' ')
        print(f'Our randomly selected word is, {chosen_word}')
        print(display)
    else:
        print("Letter don't exist")
        display.insert(x, user_query)
        print(f'\nYour made up word is {guess}',end=' ')
        print(f'Our randomly selected word is, {chosen_word}')
        print(display)




