import requests
import re
from lxml import html
from bs4 import BeautifulSoup
import re
import random


PLAYER_NAME = 1
TEAM = 2
GP = 3
MGP = 4
FGM = 5
FGA = 6
FG_PER = 7
THREE_PM = 8
THREE_PA = 9
THREE_P_PER = 10
FTM = 11
FTA = 12
FT_PER = 13
TOV = 14
PF = 15
ORB = 16
DRB = 17
RPG = 18
APG = 19
SPG = 20
BPG = 21
PPG = 22


# recuperer les informations sur les joueurs depuis un url
def sendRequest(url):
	r = requests.get(url)
	soup = BeautifulSoup(r.content, "html.parser")
	returnValue = []
	row = []

	# Recuperer les intitulés des colonnes
	for table in soup.findAll("table"):
		for th in table.findAll("th"):
			row.append(th.text)

	returnValue.append(list(row))
	# Ensuite on récupere les informations sur les joueurs
	row[:] = []

	for table in soup.findAll("table"):
		for td in table.findAll("td"):
			row.append(td.text.replace(",","."))
		returnValue.append(list(row))
		row[:] = []

	return returnValue


def searchPlayer(name):
	filepointer = open("./../res/data/playerStatistics.csv","r")
	temp = []
	for line in filepointer.readlines():
		line = line.strip("\n")
		temp = re.split(", ", line)
		if temp[PLAYER_NAME] == name:
			break
		else:
			temp = []
	filepointer.close()
	return temp

def loadTeams(fileSrc, fileDest):
	lTeams = []
	filepointer = open(fileSrc, "r")
	for line in filepointer.readlines():
		lTeams.append(line.strip("\n"))
	filepointer.close()

	filepointer = open(fileDest,"w")
	rep = sendRequest("https://en.wikipedia.org/wiki/" + lTeams[0])
	# on remplie la premiere ligne du fchier par les intutilés des colonnes
	for index in range(0, 20):
		filepointer.write(rep[0][index].replace("\n"," ").replace(",",".") + ", ")
	filepointer.write("\n")

	for team in lTeams:
		rep = sendRequest("https://en.wikipedia.org/wiki/" + team)
		for index in range(0, 20):
			filepointer.write(rep[1][index + 3].replace("\n"," ").replace	(",",".") + ", ")
		filepointer.write("\n")
	filepointer.close()


def saveData(fileName):
    filepointer = open(fileName, "w")
    l = sendRequest("https://basketball.realgm.com/nba/stats/2018/Averages/Qualified/points/All/desc/1/Regular_Season")
    index = 1;
    for e1 in l:
    	for e2 in e1:
    		filepointer.write(e2)
    		if index % 23 == 0:
    			filepointer.write("\n")
    		else:
    			filepointer.write(", ")
    		index = index + 1
    filepointer.close()



def loadGames(url, fileName):
	l = sendRequest(url)
	lines = []
	indexLine = 0
	indexColonne = 0
	filepointer = open(fileName, "w")

	# print(l[1])
	for i in range(0,10):
		filepointer.write(l[0][i].replace("\n",""))
		filepointer.write(", ")
	for e in l[1]:
		if(indexLine == 0):
			filepointer.write("\n")
			filepointer.write(l[0][indexColonne + 10].replace(","," "))
			indexColonne = indexColonne + 1
			filepointer.write(", ")

		filepointer.write(e.replace("\n"," "))
		filepointer.write(", ")
		indexLine = (indexLine + 1)%9
	filepointer.close()


def loadPlayersFromFile(fileName):
	filepointer = open(fileName, "r")
	returnValue = []
	for line in filepointer.readlines():
		line = line.strip("\n")
		returnValue.append(re.split(" ",line))

	filepointer.close()
	return returnValue

def compareListe(l1, l2, index):
	for i in range(0,min(len(l1),len(l2))):
		if l1[i] != l2[i+index]:
			return 0
	return 1

def findTargets(sentence, fileName):
	lwordIN = re.split(" ", sentence)
	lwordOUT = []
	filepointer = open(fileName, "r")
	returnValue = []
	for line in filepointer.readlines():
		line = line.strip("\n")
		lwordOUT = re.split(" ", line)
		m = min(len(lwordIN),len(lwordOUT))
		i = 0
		index = 0
		ecart = 0
		while i <= m:
			if ((i + ecart) >= len(lwordOUT) or (i + index) >= len(lwordIN)):
				break
			if lwordOUT[i+ecart].startswith('_'):
				# print(lwordOUT[i+ecart])
				l = loadPlayersFromFile("./../res/EN/voc/"+lwordOUT[i+ecart])
				for j in range(0, len(l)):
					if(compareListe(l[j], lwordIN, i+index) == 1):
						if(lwordOUT[i+ecart].startswith("__") != 1):
							returnValue.append((lwordOUT[i+ecart], " ".join(l[j])))
						if len(l[j]) >= 1:
							index = index + len(l[j]) - 1
							# ecart = ecart +
							break
			elif lwordIN[i+index] != lwordOUT[i+ecart]:
				break
			i = i + 1
	filepointer.close()
	return returnValue

def findCorrespondance(l):
	for i in range(0,len(l)):
		filepointer = open("./../res/EN/cor/" + l[i][0].replace(".txt","Correspondance.txt"),"r")
		for line in filepointer.readlines():
			line = line.strip("\n")
			# print(line)
			lline = re.split(", ", line)
			if l[i][1] in lline:
				# print(lline[0])
				l[i] = (l[i][0],lline[0])
				break
		filepointer.close()
	return l

def getInputs():
	return input("Me : ")

# def tokenization(inputs):
# 	#print(re.split(" ", inputs))
# 	return re.split(" ", inputs)
#
# def normalize(tokens):
# 	return tokens
#
# def findTargets(normalizedTokens):
# 	targets = []
# 	for t in normalizedTokens:
# 		print(t)
#
# 		isStat(t)
# 		isBWML(t)
# 		isWW(t)
# 		isPlayer(t)
# 		# verifier s'il s'agit du nom d'un joueur. si le 1er correspond verifier le 2e
# 		# ex : "LeBron James" Si on trouve "LeBron" on regarde le mot suivant "James"
# 		# sinon on verifie s'il sagit d'une statistique
# 		# sinon on verifie best / worse / most / less
# 		# sinon on verifie who / which
#
# 	return targets
#
# def getStats(targets):
# 	return
#
# def answer(statistics):
# 	return
#
def extractKey(targets):
	extraction = []
	if targets is not None:

		for t in targets:
			# print(t)
			(k,v) = t
			extraction.append(k)
	return extraction

def read_targets(fileName):
	file = open(fileName, "r")
	expectedTargets = []

	for line in file:
		line_splited = line.split(",")
		line_splited[-1] = line_splited[-1].strip()
		#print(line_splited)
		#backchannels.append(line_splited[0])
		expectedTargets.append(line_splited)
	file.close()
	return expectedTargets

def statsToNumber(str):
    switcher = {
        "gp": GP,
        "mpg": MGP,
        "fgm": FGM,
    	"fga": FGA,
    	"fg%": FG_PER,
    	"3pm": THREE_PM,
    	"3pa": THREE_PA,
    	"3pt%": THREE_P_PER,
    	"ftm": FTM,
    	"fta": FTA,
    	"ft%": FT_PER,
    	"tov": TOV,
    	"pf": PF,
    	"orb": ORB,
    	"drb": DRB,
    	"rpg": RPG,
    	"apg": APG,
    	"spg": SPG,
    	"bpg": BPG,
    	"ppg": PPG,
    }

    return switcher.get(str, -1)

def findInformations(targets):
	informations = []

	if not targets:
		print("Sorry, I did not understand your question.\nCan you rephrase it ?")
		return informations

	# targets = findCorrespondance(targets)
	extraction = extractKey(targets)
	#extraction = targets
	expectedTargets = read_targets("./../res/data/targetList.txt")
	i = 1
	for et in expectedTargets:

		#print(et)
		intersection = set(extraction).intersection(set(et))
		#print(len(intersection))
		if len(intersection) == len(extraction):
			print("traitement")
			break
		i = i + 1

	# print(i)

	if i == 1 : #ok
		print("_players.txt")

		playerName = [x[1] for x in targets if x[0] == "_players.txt"]
		print(playerName)
		player = searchPlayer(playerName[0])
		player.pop(0)

		print(player)
		couple = ("_players.txt", player[0])
		informations.append(couple)
		couple = ("_value.txt", player[1])
		informations.append(couple)
		couple = ("_statistics.txt", stat[0])
		informations.append(couple)
		couple = ("_value.txt", player[2])
		informations.append(couple)
		couple = ("_statistics.txt", stat[0])
		informations.append(couple)
		couple = ("_value.txt", player[3])
		informations.append(couple)
		couple = ("_statistics.txt", stat[0])
		informations.append(couple)
		return informations


	if i == 2 : #ok
		print("_players.txt, _link.txt")

		playerName = [x[1] for x in targets if x[0] == "_players.txt"]
		print(playerName)
		splittedName = playerName[0].split(" ")
		print(splittedName)
		link = "https://www.youtube.com/results?search_query=" + splittedName[0] + "+" + splittedName[1] + "+" + "highlights"
		print("https://www.youtube.com/results?search_query=" + splittedName[0] + "+" + splittedName[1] + "+" + "highlights")
		couple = ("_link.txt", link)
		informations.append(couple)
		couple = ("_players.txt", playerName[0])
		informations.append(couple)
		return informations

	if i == 3 :
		print("_players.txt, _bestWorse.txt")

		playerName = [x[1] for x in targets if x[0] == "_players.txt"]
		player = searchPlayer(playerName[0])
		player.pop(0)
		player.pop(0)
		player.pop(0)
		bestWorse = [x[1] for x in targets if x[0] == "_bestWorse.txt"]
		couple = ("_players.txt", playerName[0])
		informations.append(couple)

		filepointer = open("./../res/data/playerStatistics.csv","r")
		line = filepointer.readline()
		line = line.split(", ")
		line.pop(0)
		line.pop(0)
		line.pop(0)
		line[len(line)-1] = line[len(line)-1].strip()
		#print(line)

		kv = ("","")
		temp = []
		i = 0
		for p in player:
			kv = (player[i],line[i])
			temp.append(kv)
			i = i + 1

		print(kv)
		couple = ("_statistics.txt", "orb")
		informations.append(couple)
		couple = ("_bestWorse.txt", bestWorse[0])
		informations.append(couple)
		if bestWorse[0] == "best":
			couple = ("_value.txt", player[len(player)-1])
			informations.append(couple)
		else:
			couple = ("_value.txt", player[0])
			informations.append(couple)

		return informations

	if i == 4 : #ok
		print("_players.txt, _teamCity.txt")

		playerName = [x[1] for x in targets if x[0] == "_players.txt"]
		player = searchPlayer(playerName[0])
		print(player[TEAM])

		couple = ("_players.txt", playerName[0])
		informations.append(couple)
		couple = ("_teamCity.txt", player[TEAM])
		informations.append(couple)

		return informations

	if i == 5 : #ok
		print("_statistics.txt, _players.txt, _value.txt")

		playerName = [x[1] for x in targets if x[0] == "_players.txt"]
		player = searchPlayer(playerName[0])
		stat = [x[1] for x in targets if x[0] == "_statistics.txt"]
		print(stat[0])
		print(statsToNumber(stat[0]))
		print(player[statsToNumber(stat[0])])

		couple = ("_statistics.txt", stat[0])
		informations.append(couple)
		couple = ("_players.txt", playerName[0])
		informations.append(couple)
		couple = ("_value.txt", player[statsToNumber(stat[0])])
		informations.append(couple)
		return informations

	if i == 6 : #ok
		print("_statistics.txt, _bestWorse.txt, _value.txt")
		stat = [x[1] for x in targets if x[0] == "_statistics.txt"]
		bestWorse = [x[1] for x in targets if x[0] == "_bestWorse.txt"]
		filepointer = open("./../res/data/playerStatistics.csv","r")
		temp = []
		kv = (0,"")
		i = 0
		for line in filepointer:

			line_splited = line.split(", ")
			line_splited[-1] = line_splited[-1].strip()

			kv = (line_splited[statsToNumber(stat[0])],line_splited[PLAYER_NAME])
			temp.append(kv)
			i = i + 1
		temp.pop(0)
		temp.sort(key=lambda tup: tup[0])
		if bestWorse[0] == "best":
			kv = temp[len(temp)-1]
		else:
			kv = temp[0]
		playerName = kv[1]
		print(playerName)
		print(kv[0])
		player = searchPlayer(playerName)
		playerName = player[1]
		# print(player)
		#print(temp)

		couple = ("_statistics.txt", stat[0])
		informations.append(couple)
		couple = ("_bestWorse.txt", bestWorse[0])
		informations.append(couple)
		couple = ("_value.txt", kv[0])
		informations.append(couple)
		couple = ("_players.txt", playerName)
		informations.append(couple)

		return informations

	if i == 7 : #ok
		print("_statistics.txt, _mostLess.txt, _value.txt")
		stat = [x[1] for x in targets if x[0] == "_statistics.txt"]
		mostLess = [x[1] for x in targets if x[0] == "_mostLess.txt"]
		filepointer = open("./../res/data/playerStatistics.csv","r")
		temp = []
		kv = (0,"")
		i = 0
		for line in filepointer:
			#temp.append((line[statsToNumber(stat[0])]),i)
			# if i == 1:
			# 	continue
			line_splited = line.split(", ")
			line_splited[-1] = line_splited[-1].strip()
			kv = (line_splited[statsToNumber(stat[0])],line_splited[PLAYER_NAME])
			temp.append(kv)
			i = i + 1
		temp.pop(0)
		temp.sort(key=lambda tup: tup[0])
		if mostLess[0] == "most":
			kv = temp[len(temp)-1]
		else:
			kv = temp[0]
		playerName = kv[1]
		print(playerName)
		print(kv[0])
		player = searchPlayer(playerName)
		playerName = player[1]
		# print(player)
		#print(temp)

		couple = ("_statistics.txt", stat[0])
		informations.append(couple)
		couple = ("_mostLess.txt", mostLess[0])
		informations.append(couple)
		couple = ("_value.txt", kv[0])
		informations.append(couple)
		couple = ("_players.txt", playerName)
		informations.append(couple)

		return informations

	if i > 7:
		print("Sorry, I did not understand your question.\nCan you rephrase it ?")

def statsToNumber(str):
    switcher = {
        "gp": GP,
        "mpg": MGP,
        "fgm": FGM,
    	"fga": FGA,
    	"fg%": FG_PER,
    	"3pm": THREE_PM,
    	"3pa": THREE_PA,
    	"3pt%": THREE_P_PER,
    	"ftm": FTM,
    	"fta": FTA,
    	"ft%": FT_PER,
    	"tov": TOV,
    	"pf": PF,
    	"orb": ORB,
    	"drb": DRB,
    	"rpg": RPG,
    	"apg": APG,
    	"spg": SPG,
    	"bpg": BPG,
    	"ppg": PPG,
    }

    return switcher.get(str, -1)



# TODO

# faire une fonction qui permet de retrouver la phrase réponse.
# Pour cela je parcours la liste des tuples et je vérifie que tous les elemnts du premier tuple dans la phrase.
# je fais sa pour tout le fichier
# cela permet de recuperer toutes les phrases que je peux renvoyer au client
# je choisis une parmis eux cela aide a faire du random

def findAnswer(fileName, lPairs):
	filepointer = open(fileName, "r")
	returnValue = []
	for line in filepointer.readlines():
		newAnswer = True
		line = line.strip("\n")
		lword = re.split(" ", line)
		for i in range(0,len(lPairs)):
			if lPairs[i][0] not in lword:
				newAnswer = False
				break
		if newAnswer :
			returnValue.append(line)
	filepointer.close()
	return returnValue


def buildAnswer(lPairs):
	lAnswer = findAnswer("./../res/EN/ans/answers.txt", lPairs)
	# if lAnswer == [] :
	# 	return ""
	answerSelected = random.choice(lAnswer)
	for i in range(0,len(lPairs)):
		answerSelected = answerSelected.replace(lPairs[i][0],lPairs[i][1],1)
	return answerSelected



def nba_assistant():
	print("Welcome ! My name is NBA Assistant !")
	print("I'm here to give you informations and statistics about the NBA !")
	print("What would you like to know ?")
	# while 1:
	# 	inputs = getInputs()
	# 	targets = findTargets(inputs, "./../res/EN/voc/accepted_sentences.txt")
	# 	normalizedTokens = findCorrespondance(targets)
	# 	print(normalizedTokens)
	# 	preIns = findInformations(normalizedTokens)
	# 	print(preIns)
	# 	print(buildAnswer(preIns))

		# tokens = tokenization(inputs)
		# normalizedTokens = normalize(tokens)
		# targets = findTargets(normalizedTokens)
		# statistics = getStats(targets)
		# ans = answer(statistics)
	info =findInformations([("_players.txt", "James Harden"),("_bestWorse.txt", "best")])
	print(info)
	# saveData("./../res/data/playerStatistics.csv")
	# loadGames("https://www.basketball-reference.com/leagues/NBA_2018_games.html", "./../res/data/gameInfo.csv")
	# loadTeams("./../res/data/teamList.txt","./../res/data/TeamInfo.csv")
	# print("How many defensive rebound James Harden average ?")
	# print(findCorrespondance(findTargets("How many defensive rebound James Harden average ?","./../res/EN/voc/accepted_sentences.txt")))
	# print("In what category is Taurean Prince the best ?")
	#print(findCorrespondance(findTargets("In what category is Taurean Prince the best ?","./../res/EN/voc/accepted_sentences.txt")))
	# print("\n\nIn which team does Taurean Prince play ?")
	# print(findCorrespondance(findTargets("In which team does Taurean Prince play ?","./../res/EN/voc/accepted_sentences.txt")))
	# print(searchPlayer("James Harden "))
	# print(findCorrespondance(findTargets("I want to know Who is the best player in defensive rebound ?","./../res/EN/voc/accepted_sentences.txt")))
	# print(findAnswer("./../res/EN/ans/answers.txt",[("_player","TOTO BOBO"),("_statistics","drb"), ("+value","32")]))
	# print(buildAnswer([("_player","TOTO BOBO"),("_statistics","drb"), ("+value","32")]))
	# __want.txt Who is the _bw.txt player in _statistic.txt ?
	# print(statsToNumber("spg"))

if __name__=="__main__":
	nba_assistant()
