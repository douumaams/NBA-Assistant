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
            #print(lword[:])
            inputs.append(lword[:])
            lword.clear()
            continue
        lword.append(line.strip("\n"))
    inputs.append(lword[:])
    filepointer.close()
    #print(inputs)
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
    
    

def read_voc():
    ltopic = []
    lvoc = []

    #family
    filepointer = open("./../res/EN/familyVoc.txt","r")
    for line in filepointer.readlines():
        lvoc.append(line.strip("\n"))

    ltopic.append(lvoc[:])
    lvoc.clear()
    filepointer.close()

    #sport
    filepointer = open("./../res/EN/sportVoc.txt","r")
    for line in filepointer.readlines():
        lvoc.append(line.strip("\n"))

    ltopic.append(lvoc[:])
    lvoc.clear()
    filepointer.close()

    #cooking
    filepointer = open("./../res/EN/cookingVoc.txt","r")
    for line in filepointer.readlines():
        lvoc.append(line.strip("\n"))

    ltopic.append(lvoc[:])
    lvoc.clear()
    filepointer.close()

    #computerScience
    filepointer = open("./../res/EN/computerScienceVoc.txt","r")
    for line in filepointer.readlines():
        lvoc.append(line.strip("\n"))

    ltopic.append(lvoc[:])
    lvoc.clear()
    filepointer.close()

    #motorcycle
    filepointer = open("./../res/EN/motorcycleVoc.txt","r")
    for line in filepointer.readlines():
        lvoc.append(line.strip("\n"))

    ltopic.append(lvoc[:])
    lvoc.clear()
    filepointer.close()

    print(ltopic)
    return ltopic

def read_ans():
    ltopic = []
    lans = []

    #family
    filepointer = open("./../res/EN/familyAns.txt","r")
    for line in filepointer.readlines():
        lans.append(line.strip("\n"))

    ltopic.append(lans[:])
    lans.clear()
    filepointer.close()

    #sport
    filepointer = open("./../res/EN/sportAns.txt","r")
    for line in filepointer.readlines():
        lans.append(line.strip("\n"))

    ltopic.append(lans[:])
    lans.clear()
    filepointer.close()

    #cooking
    filepointer = open("./../res/EN/cookingAns.txt","r")
    for line in filepointer.readlines():
        lans.append(line.strip("\n"))

    ltopic.append(lans[:])
    lans.clear()
    filepointer.close()

    #computerScience
    filepointer = open("./../res/EN/computerScienceAns.txt","r")
    for line in filepointer.readlines():
        lans.append(line.strip("\n"))

    ltopic.append(lans[:])
    lans.clear()
    filepointer.close()

    #motorcycle
    filepointer = open("./../res/EN/motorcycleAns.txt","r")
    for line in filepointer.readlines():
        lans.append(line.strip("\n"))

    ltopic.append(lans[:])
    lans.clear()
    filepointer.close()

    print(ltopic)
    return ltopic

def analyse(sentence):
    outputs = read_inputs("./../res/EN/outputs.txt")
    #print(outputs)
    inputs = read_inputs("./../res/EN/inputs.txt")
    #print(inputs)
    vocs = read_voc()
    ans = read_ans()
    response = "Why "
    request = ""
    s = re.split(" ", sentence)
    #print(s)
    for i in range(len(inputs)):
        #print(inputs[i][0])
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
    if response == "Why ":
    	print("jaja")
    else:
    	print("Bot: " + response + " " + sentence.strip(request) + "?")
# 
if __name__=="__main__":
    chatbot()
    # read_voc()
    # read_ans()
