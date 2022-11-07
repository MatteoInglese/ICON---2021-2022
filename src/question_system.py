# -*- coding: utf-8 -*-
def ask(qst: str) -> bool:
    ans = input(qst + " (y/n): ")
    ans = ans.lower()
    
    while not correct_ans(ans):
        print("Il valore inserito non è una risposta valida!")
        ans = input(qst + " (y/n): ")

    return ans == "y"


def correct_ans(ans: str) -> bool:
    return ans == "y" or ans == "n" or ans == "yes" or ans == "no"