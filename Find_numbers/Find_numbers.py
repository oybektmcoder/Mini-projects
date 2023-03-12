import random as rn
#print(rn.randint(0, 10+1))
def find_number_pc(n):
    l=0
    num=rn.randint(0, n+1)
    print(f"\n\nLets play find number me from 0 to {n}")
    f=True
    while(f):
        l += 1 
        n=int(input("Input your about number:"))
        if(n==num):
            print(f"\n\nYou find after {l} steps ..... ")
            f=False
            break
        elif(n<num):
            print("My number is bigger than yours (+)")
        elif(n>num):
            print("My number is smaller than yours (-)")
    return l

def find_number_me(n):
    l=0
    r=n
    num=rn.randint(0, n+1)
    n=0
    print(f"You think one number I will try range of {n} \n I send number you said Ok \n if my number smaller than yours,send + \n if my number bigger than yours,send me -")
    while True:
        n+=1
        m=(l+r)//2
        ab_n=input(f"You think:{m} is is: ")
        ab_n.lower()
        if(ab_n=='ok'):
            print(f"I find after {n}-steps")
            break
        elif(ab_n=='+'):
            l=m
        elif(ab_n=='-'):
            r=m
    return n     
def play_find(x=10):
    while True:
        
        approximately_me=find_number_me(x)
        approximately_pc=find_number_pc(x)
        
        if(approximately_me > approximately_pc):
            print("\n\nThe men is winner by steps\n\n")
        elif(approximately_me < approximately_pc):
            print("\n\nThe PC is winner by steps\n\n")
        elif(approximately_me == approximately_pc):
            print("All winner")
            print(f"pc={approximately_pc} \nme:{approximately_me} \n\n")
play_find()
            
            
        
        
    
    
    