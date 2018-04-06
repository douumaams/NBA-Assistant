import os
import random
import requests
from random import randint

def chatbot(backchannels):
	print("Welcome my name is Backchannels Bot ! I'm here to backchannel whatever you say !")
	result = ("uh uh", 0)
	while 1:
		human = input("Me : ")
		result = chooseBackchannel(result[1],backchannels)
		print(result[0])


def chooseBackchannel(previous, backchannels):

	n = randint(0,len(backchannels)-1)
	while n == previous:
		n = randint(0,len(backchannels)-1)

	return "Bot : " + backchannels[n], n

def read_backchannels(fileName):
	file = open(fileName, "r")
	backchannels = []

	for line in file:
		line_splited = line.split("\n")
		backchannels.append(line_splited[0])

	file.close()
	return backchannels

if __name__=="__main__":
	backchannels = read_backchannels("./../res/backchannels.txt")
	chatbot(backchannels)
