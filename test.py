#!/usr/bin/python3

def reverse():
    user = input("Entrez votre mot à renverser: ")
    reverse ="".join(reversed(user))
    print(reverse)


  ponc = ['!','#','?',',','.',':','"',';']

def countwords():
    user = input("Entrez votre proposition: ")
    for p in ponc:
        if user == p:
            p = " "
    word_count = len(user.split())
    print(word_count)





i
