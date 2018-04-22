import os
import random
import requests
from random import randint

def firstMode(backchannels):
	print("Welcome my name is Backchannels Bot ! I'm here to backchannel whatever you say !")
	while 1:
		human = input("Me : ")
		print(chooseBackchannel(backchannels))


def chooseBackchannel(backchannels):
	n = randint(0,len(backchannels))
	return "Bot : " + backchannels[n]

"""def intermediateMode():


def advancedMode():"""




def read_backchannels(fileName):
	file = open(fileName, "r")
	backchannels = []
	for line in file:

		line_splited = line.split("\n")
		backchannels.append(line_splited[0])
		"""line_splited = line.split(":")
		if(len(line_splited) < 2):
			continue
		if(line_splited[0] in backchannels):
			backchannels[line_splited[0]].append(line_splited[1])
		else:
			backchannels[line_splited[0]] = [line_splited[1]]"""

	file.close()
	return backchannels

# https://basketball.realgm.com/nba/stats
def send_request(url):
	r = requests.get(url)
	print(r.text)


if __name__=="__main__":
	backchannels = read_backchannels("./../res/backchannels.txt")
	#print(backchannels)
	firstMode(backchannels)
	#send_request("https://basketball.realgm.com/nba/stats")

