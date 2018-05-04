import os
import random
import requests
import re
from random import randint

def chatbot():
    print("Welcome my name is Backchannels Bot ! I'm here to backchannel whatever you say !")
    lans = []
    while 1:
        human = input("Me : ")
        analyse(human, lans)
        if len(lans) > 2:
            lans = lans[len(lans)-1:]

        #print(lans)


def analyse(sentence, lans):
    ans = discussion(sentence, lans)
    if ans == "":
        ans = eliza(sentence,lans)

    lans.append(ans)

    print("Bot: " + ans)


def eliza(sentence, lans):
    outputs = read_inputs("./../res/EN/outputs.txt")
    #print(outputs)
    inputs = read_inputs("./../res/EN/inputs.txt")

    #print(inputs)
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
    if response == "Why ":
        #return "backchannel"
        backchannel = chooseBackchannel()

        while backchannel == lans:
            backchannel = chooseBackchannel()
        #print(backchannel)
        return backchannel
    else:
    # ... la suite de la phrase

    #print("Bot: " + response + " " + sentence.strip(request) + "?")
        return response + " " + sentence.strip(request) + "?"

def discussion(sentence, lans):
    answer = ""
    topic = ""

    splittedSentence = re.split(" ", sentence)
    #print(splittedSentence)

    for word in splittedSentence:
        topic = findKeyword(word)
        #print("topic : " + topic)
        if topic != "":
            break

    if topic != "":

        answer = selectRandom(topic)

        if lans:
            while answer == lans[-1]:
                #print("bonjour")
                answer = selectRandom(topic)
    #print("answer : " + answer)
    return answer

def findKeyword(word):
    vocs = read_voc()

    for ltopic in vocs:
        for keyword in ltopic:
            if word == keyword:
                return ltopic[0]
    return ""

def selectRandom(topic):
    ans = read_ans()

    for ltopic in ans:
        if topic == ltopic[0]:
            #print(topic)
            n = randint(1,len(ltopic)-1)
            return ltopic[n] #answer

def chooseBackchannel():
    backchannels = read_backchannels("./../res/EN/backchannels.txt")
    n = randint(0,len(backchannels)-1)

    #print(backchannels[n])
    return backchannels[n]

def read_backchannels(fileName):
	file = open(fileName, "r")
	backchannels = []

	for line in file:
		line_splited = line.split("\n")
		backchannels.append(line_splited[0])

	file.close()
	return backchannels

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

def read_file(path):
    l = []
    filepointer = open(path,"r")
    for line in filepointer.readlines():
        l.append(line.strip("\n"))

    filepointer.close()
    return l

def read_voc():

    ltopic = []

    ltopic.append(read_file("./../res/EN/familyVoc.txt"))
    ltopic.append(read_file("./../res/EN/sportVoc.txt"))
    ltopic.append(read_file("./../res/EN/cookingVoc.txt"))
    ltopic.append(read_file("./../res/EN/computerScienceVoc.txt"))
    ltopic.append(read_file("./../res/EN/motorcycleVoc.txt"))

    return ltopic

def read_ans():

    ltopic = []

    ltopic.append(read_file("./../res/EN/familyAns.txt"))
    ltopic.append(read_file("./../res/EN/sportAns.txt"))
    ltopic.append(read_file("./../res/EN/cookAns.txt"))
    ltopic.append(read_file("./../res/EN/computerScienceAns.txt"))
    ltopic.append(read_file("./../res/EN/motorcycleAns.txt"))

    return ltopic

if __name__=="__main__":
    chatbot()
    #read_voc()
    #read_ans()
