import requests
import re
from lxml import html
from bs4 import BeautifulSoup
import re


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
	filepointer = open("./ici.csv","r")
	temp = []
	for line in filepointer.readlines():
		line = line.strip("\n")
		temp = re.split(", ", line)
		if temp[PLAYER_NAME] == name:
			break
	filepointer.close()
	return temp

# lien pour la liste des equipes
# https://en.wikipedia.org/wiki/List_of_current_NBA_team_rosters
# def loadTeams(url):
# 	# r = requests.get(url)
# 	# soup = BeautifulSoup(r.content, "html.parser")
# 	returnValue = []
# 	# row = []
# 	# table = soup.findAll("table")
# 	# return table
# 	# for th in table[0].findAll("th"):
# 	# 	row.append(th.text)

# 	# returnValue.append(list(row))
# 	# row[:] = []

# 	# for td in table.findAll("td"):
# 	# 	row.append(td.text)
# 	# returnValue.append(row)
# 	# return returnValue
# 	l = sendRequest(url)
# 	# returnValue.append(l[:17])
# 	for x in range(0,20):
# 		print("" + l[0][x] + "============>" + l[1][x + 3])


# 	# returnValue.append(l[4:22])
# 	# return returnValue


# (loadTeams("https://en.wikipedia.org/wiki/Boston_Celtics"))
# print(sendRequest("https://en.wikipedia.org/wiki/Atlanta_Hawks")[1])

def loadTeams(teamNamesFile, teamNamesInfoFile):
	lTeams = []
	filepointer = open(teamNamesFile, "r")
	for line in filepointer.readlines():
		lTeams.append(line.strip("\n"))
	filepointer.close()

	filepointer = open(teamNamesInfoFile,"w")
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



# loadTeams("./../res/EN/TeamNames.txt","./test.csv")
  #   for x in range(0, 20):
		# print("" + l[0][x] + "============>" + l[1][x + 3])


#TODO:
#	- Recuperer les données e wikipédia
#	- proposer le bon joueur si l'utilisateur se trompe dans l'ecriture du nom
#	- Faire les correspondance entre les termes NBA t les termes que l'utilisateur peut utiliser
#	-
#
#





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

	print(l[1])
	for i in range(0,10):
		filepointer.write(l[0][i].replace("\n",""))
		filepointer.write(", ")
	for e in l[1]:
		if(indexLine == 0):
			filepointer.write("\n")
			# print("\n")
			# print("\n\n\n\n---------------------------------------------------------------------")
			# print(l[0][indexColonne + 9])
			filepointer.write(l[0][indexColonne + 10].replace(","," "))
			indexColonne = indexColonne + 1
			filepointer.write(", ")

		filepointer.write(e.replace("\n"," "))
		filepointer.write(", ")
		indexLine = (indexLine + 1)%9
	# 	print(e)
		# print([l[0][indexLine*indexColonne+9]])
		# lines.append([l[0][indexLine]].append(e))
		# indexLine = (indexLine+1) % 9
		# if indexLine
	# print(lines)
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

# l = loadPlayersFromFile("exemplejoueur.txt")
# print(compareListe(l[0],l[0],0))
# print(loadPlayersFromFile("exemplejoueur.txt"))

# def findTargets(sentence, fileName):
# 	lwordIN = re.split(" ", sentence)
# 	lwordOUT = []
# 	filepointer = open(fileName, "r")
# 	returnValue = []
# 	for line in filepointer.readlines():
# 		line = line.strip("\n")
# 		lwordOUT = re.split(" ", line)
# 		for i in range(0,min(len(lwordIN),len(lwordOUT))):
# 			if re.match("_.*",lwordOUT[i]) is not None :
# 				l = loadPlayersFromFile("./../res/EN/"+lwordOUT[i])
# 				# print(l)
# 				for j in range(0, len(l)):
# 					# print(l)
# 					if(compareListe(l[j], lwordIN, i)):
# 						print(l[j])
# 						print("----------------")
# 						print(lwordIN[i+2])
# 						returnValue.append((lwordOUT[i],l[j]))
# 						i = i + len(l[j])
# 						print(len(l[j]))
# 						break
# 				# faut modifier la boucle for en while
# 					# load le fichier sous forme de liste de liste
# 					# une fonction qui prend 2 liste et un indice et compare les elements.
# 			elif lwordIN[i] != lwordOUT[i]:
# 				break
# 	filepointer.close()
# 	return returnValue


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
				# print(l)
				# print(i+index)
				# print(i+ecart)
				for j in range(0, len(l)):
					# print(l)
					if(compareListe(l[j], lwordIN, i+index) == 1):
						# print(lwordIN[i+index]+"--------"+lwordOUT[i+ecart])
						# print(l[j])
						returnValue.append((lwordOUT[i+ecart], " ".join(l[j])))
						# i = i + len(l[j])
						if len(l[j]) > 1:
							index = index + len(l[j]) - 1
							ecart = ecart
						# print(len(l[j]))
						# print(i + index)
						# print(i + ecart)
						# print("-------------------------")
						# print(lwordOUT[i+ecart])
						# print("MyINDEX = "+ str(index))
						# print(lwordIN[i])
						# print(len(l[j]))
						# break
					# else:
					# 	print(l[j])
					# 	print(lwordIN[i+index])
					# 	print("___________________________________________________\n")
					# 	print(lwordIN[i+index+1])
					# 	print("\n\n\n\n\n_________________________________________________________")
				# faut modifier la boucle for en while
					# load le fichier sous forme de liste de liste
					# une fonction qui prend 2 liste et un indice et compare les elements.
			elif lwordIN[i+index] != lwordOUT[i+ecart]:
				break


			# print("index = " + str(index))
			# print(index)
			i = i + 1
	filepointer.close()
	return returnValue

def findCorrespondance(l):
	for i in range(0,len(l)):
		filepointer = open("./../res/EN/cor/" + l[i][0].replace(".txt","Correspondance.txt"),"r")
		for line in filepointer.readlines():
			line = line.strip("\n")
			lline = re.split(", ", line)
			if l[i][1] in lline:
				print(lline[0])
				l[i] = (l[i][0],lline[0])
				break
		filepointer.close()
		return l
# print("In what category is Taurean Prince the best ?")
# print(findCorrespondance(findTargets("In what category is Taurean Prince the best ?","./../res/EN/accepted_sentences.txt")))
# print("\n\nIn which team does Taurean Prince play ?")
# print(findCorrespondance(findTargets("In which team does Taurean Prince play ?","./../res/EN/accepted_sentences.txt")))
print("\n\nHow many defensive rebound James Harden average ?")
print(findCorrespondance(findTargets("How many defensive rebound James Harden average ?","./../res/EN/voc/accepted_sentences.txt")))
# print(loadPlayersFromFile("./../res/EN/_statistics.txt"))
# 	filepointer.close()


# loadGames("https://www.basketball-reference.com/leagues/NBA_2018_games.html", "test2.csv")
# loadGames("https://www.basketball-reference.com/leagues/NBA_2018_games-november.html", "test_november.csv")


# saveData("./ici.csv")
# def loadData(url):
# print(searchPlayer("Kevin Durant"))



# l = sendRequest("https://en.wikipedia.org/wiki/Boston_Celtics")
# l = sendRequest("https://basketball.realgm.com/nba/stats/2018/Averages/Qualified/points/All/desc/1/Regular_Season")

# soup = BeautifulSoup(l[1][1],"lxml")

# print(l)
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
