
import random

word_generator=["apple","mango","peach","passion","kiwi"]
random_selector=random.choice(word_generator)
word_length=len(random_selector)

#generating banks
blanks=[]

for x in range(0,word_length):
    blanks+='_'
    #print(blanks)

print(f"Hint: Our Mystery Word Is: {random_selector}")
print((2**5)*'-')
print(blanks)
#user_input=input(print("Guess the letters making up the mystery word"))
#user_input.lower()

for y in range(0,word_length):
    letter=random_selector[y]
    #print(letter,end="")
    user_input = input(print("Guess the letters making up the mystery word"))
    user_input.lower()
    if letter==user_input:
        print("Correct Guess")
        blanks[y]=user_input
        print(blanks)
    else:
        print("Incorrect Guess!")
        blanks[y] = user_input
        print(blanks)


