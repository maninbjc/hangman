# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 05:21:14 2019

@author: szkma
"""
import random

def hangman(word):
    wrong = 0
    stages = ["",
              "__________          ",
              "|                   ",
              "|         |         ",
              "|         O         ",
              "|        /|\        ",
              "|        / \        ",
              "|                   "
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcom to Hangman!")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Guess one letter: "
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = "$"
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("\nYou Win!\n")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("You Lose! The answer is {}.".format(word))

if __name__ == "__main__":
    wordlist = ["Apple", "Banana", "Orange", "Melon", "Grape"]
    w_ind = random.randint(0,len(wordlist))
    word = wordlist[w_ind]
    hangman(word)