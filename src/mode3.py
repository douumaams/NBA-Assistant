import requests
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
				l = loadPlayersFromFile("./../res/EN/"+lwordOUT[i+ecart])
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
		filepointer = open("./../res/EN/Cor/" + l[i][0].replace(".txt","Correspondance.txt"),"r")
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
# print("\n\nHow many defensive rebound James Harden average ?")
# print(findCorrespondance(findTargets("How many defensive rebound James Harden average ?","./../res/EN/accepted_sentences.txt")))
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


# saveData("./../res/data/playersStatistics.csv")
loadGames("https://www.basketball-reference.com/leagues/NBA_2018_games.html", "./../res/data/gamesInfo.csv")
# loadTeams("./../res/EN/TeamNames.txt","./../res/data/TeamsInfo.csv")
