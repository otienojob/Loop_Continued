import random

#word list
chosen_word=[]
word_list=["avocado","baboon","camel"]
chosen_word.append(random.choice(word_list))
holding_letter=""

print(((2**6)*'..'))
print(f'Hint: Our randomly generated word is, {chosen_word}\n')

blanks=[]

word_length=len(chosen_word)

for x in range(word_length):
    blanks.append('-')
guess="" #created a holding variable for every guessed letter by users

print("Lets play a guessing game. You guess a letter and we check if it makes up one of the letters in our randomly generated word!\n")
print(blanks)


user_query=input(print(f"Guess a 'letter' or character making our mystery word. You have {word_length} guesses"))
user_query.lower()
guess += user_query
#creating blanks for every randomly selected word


#loop statement to count number of guesses that is equal to chosen random word
for y in chosen_word:
    holding_letter=chosen_word[y]
    print(f'First guess is, {user_query}, while {y} mystery word is {chosen_word(y)}')
    user_query=input(print(f"\n Guess a 'letter' or character making a word. You have {y} guesses remaining"))
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




