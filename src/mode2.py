import os
import random
import requests
import re
from random import randint



def chatbot():
    print("Welcome my name is Backchannels Bot ! I'm here to backchannel whatever you say !")
    result = ("uh uh", 0)
    while 1:
        human = input("Me : ")
        analyse(human)
        # if(xxx(human) == 1):
        #     print("La famille est trés importante")

def read_inputs(fileName):
    inputs = []
    lword = []
    filepointer = open(fileName, "r")
    for line in filepointer.readlines():
        if line.strip() == "":
            inputs.append(lword[:])
            lword.clear()
            continue
        lword.append(line.strip("\n"))
    inputs.append(lword[:])
    filepointer.close()
    return inputs


def xxx(sentence):
    familyVoc = []
    filepointer = open("./../res/EN/familyVocabulary.txt", "r")
    lword = sentence.split(" ")
    for line in filepointer:
        if(line.strip("\n") in familyVoc):
            filepointer.close()
            print(line.strip + ":" +familyVocabulary)
            return 1
        
    filepointer.close()
    return 0

    #     familyVoc.append(line.strip("\n"))
    # for word in lword:
    #     if word in familyVoc:
    #         return 1
    # print(familyVoc)
    # print(lword)
    # return 0
    # pickle, load, dump
    # pour les petites données on peut utiliser json
    
    


def analyse(sentence):
    outputs = read_inputs("./../res/EN/outputs.txt")
    inputs = read_inputs("./../res/EN/inputs.txt")
    print(inputs)
    response = "Why "
    request = ""
    s = re.split(" ", sentence)
    for i in range(len(inputs)):
        if(s[0] == inputs[i][0]):
            for j in range(len(inputs[i])):
                tense = s[1]
                if(s[1] == "will" and s[2] in ["be", "have"]):
                    tense = s[1]+ " " +s[2] 
                if(tense == inputs[i][j]):
                    request = s[0]+" "+tense 
                    response += outputs[i][j]
                    break;


    # ... la suite de la phrase
    # print(request)
    # print(inputs)
    print("Bot: "+response + " " + sentence.strip(request) + "?")



if __name__=="__main__":
    chatbot()
	