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
    filepointer.close()
    return inputs

def analyse(sentence):
    outputs = read_inputs("./../res/EN/outputs.txt")
    inputs = read_inputs("./../res/EN/inputs.txt")
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
    print(response + " " + sentence.strip(request) + "?")



if __name__=="__main__":
    chatbot()
	