
import random

word_generator=["apple","mango","peach","passion","kiwi"]
random_selector=random.choice(word_generator)
word_length=len(random_selector)

#generating banks
blanks=[]

for x in range(0,word_length):
    blanks+='_'
    print(blanks)

print(f"Hint: Our Mystery Word Is: {random_selector}")
user_input=print("")
