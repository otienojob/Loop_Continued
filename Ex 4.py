import random
chosen_word=""
word_list=["camel","baboon","monkey","cow"]
chosen_word=random.choice(word_list)

print((2**6)*'...')
print(f"Hint: Our randomly generated word is, {chosen_word}")
print("")
print("Let's play a guess a letter game. Guess a random letter making up our mystery word!")

blank=[]
word_length=len(chosen_word)


for x in chosen_word:
    blank+="-"

user_guess=input(print(f"Let's fill in the blanks by guessing a letter, {blank}"))
user_guess.lower()

for y in range(word_length):
    our_letter=chosen_word[y]
    print(f"Current Position: {y} \n Current Letter: {our_letter} \n Guessed Letter {user_guess}")
    if our_letter==user_guess:
        print("The letter exists")
        blank[y]=our_letter
        continue
    else:
        print("Incorrect Guess")
        blank[y]=user_guess
print(blank)



