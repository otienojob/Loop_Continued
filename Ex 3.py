import random

#word list
word_list=["avocado","baboon","camel"]

#randomly selected word from the initial list
chosen_word=random.choice(word_list)
print(((2**6)*'..'))
print(f'The randomy generated word is, {chosen_word}\n')

guess="" #created a holding variable for every guessed letter by users

#loop statement to count number of guesses that is equal to chosen random word
for x in len(chosen_word)

print("Lets play a guessing game. You guess a letter and we check if it makes up one of the letters in our randomly generated word!\n")
user_query=input(print("Guess a 'letter' or character making a word: "))

guess=user_query.lower()


print(f'You entered, {guess}. Checking')
if guess in chosen_word:
    print("Letter exist")
else:
    print("Letter don't exist")




