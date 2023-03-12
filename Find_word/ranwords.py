from uzwords import words
import random as ab 
def get_word():
    word=ab.choice(words)
    while "-" in word or " " in word:
        word=ab.choice(words)
    word=word.upper()
    return word

def display(user_letter,word):
    display_word=""
    for letter in word:
        if letter.upper() in user_letter.upper():
            display_word +=letter
        else:
            display_word +='-'
    return display_word

def play():
    num=0
    word=get_word()
    word_letters=set(word)
    user_letters=''
    print(f"I think a word which is lenght of {len(word)}")
    while len(word_letters)>0:
        print(display(user_letters,word))
        if user_letters:
            print(f"Untill now you send me {user_letters.upper()}")
        
        letter=input("Yours probobly letter:").upper()
        if letter in user_letters:
            print(f"You send me this letter......")
            continue
        elif(letter in word):
            word_letters.remove(letter)
            print(f"You find correctly...")
        else:
            print("Error,You have anather chance..")
        user_letters +=letter
    num=len(user_letters)
    print(f"Congratulation.\nYou are winner after {num} steps")
play()
        
        
        
        
        
        
        
        
        
        
        
        
        
play()