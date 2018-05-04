import requests
import re
from lxml import html
from bs4 import BeautifulSoup


# recuperer les informations sur les joueurs depuis un url
def sendRequest(url):
	r = requests.get(url)
	soup = BeautifulSoup(r.content, "html.parser")
	returnValue = []
	row = []

	# Recuperer les intitulés des colonnes
	for table in soup.findAll("table"):
		for th in table.findAll("th"):
			row.append(th)

	returnValue.append(list(row))
	# Ensuite on récupere les informations sur les joueurs
	row[:] = []

	for table in soup.findAll("table"):
		for td in table.findAll("td"):
			row.append(td)
		returnValue.append(list(row))
		row[:] = []

	return returnValue

l = sendRequest("https://en.wikipedia.org/wiki/Boston_Celtics")
# l = sendRequest("https://basketball.realgm.com/nba/stats/2018/Averages/Qualified/points/All/desc/1/Regular_Season")

# soup = BeautifulSoup(l[1][1],"lxml")

#print(l)
# print(sendRequest("https://basketball.realgm.com/nba/stats/2018/Averages/Qualified/points/All/desc/2/Regular_Season"))
# def getInputs():
# 	return input("Me : ")
#
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
	for t in targets:
		print(t)
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

def findInformations(targets):
	# extraction = extractKey(targets)
	extraction = targets
	expectedTargets = read_targets("./../res/EN/targetList.txt")
	i = 1
	for et in expectedTargets:

		#print(et)
		intersection = set(extraction).intersection(set(et))
		#print(len(intersection))
		if len(intersection) == len(extraction):
			print("traitement")
			break
		i = i + 1

	print(i)
	if i == 1 : print("_players.txt")
	if i == 2 : print("_players.txt, _video.txt")
	if i == 3 : print("_players.txt, _bestWorse.txt")
	if i == 4 : print("_players.txt, _teamCity.txt")
	if i == 5 : print("_statistics.txt, _players.txt")
	if i == 6 : print("_statistics.txt, _bestWorse.txt")
	if i == 7 : print("_statistics.txt, _mostLess.txt")
	return i


def nba_assistant():
	# print("Welcome ! My name is NBA Assistant !")
	# print("I'm here to give you informations and statistics about the NBA !")
	# print("What would you like to know ?")
	# while 1:
	# 	inputs = getInputs()
	# 	tokens = tokenization(inputs)
	# 	normalizedTokens = normalize(tokens)
	# 	targets = findTargets(normalizedTokens)
	# 	statistics = getStats(targets)
	# 	ans = answer(statistics)
	findInformations(["_video.txt", "_players.txt"])

if __name__=="__main__":
	nba_assistant()
