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



loadTeams("./../res/EN/TeamNames.txt","./test.csv")
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

# saveData("./ici.csv")
# def loadData(url):
# print(searchPlayer("Kevin Durant"))



# l = sendRequest("https://en.wikipedia.org/wiki/Boston_Celtics")
# l = sendRequest("https://basketball.realgm.com/nba/stats/2018/Averages/Qualified/points/All/desc/1/Regular_Season")

# soup = BeautifulSoup(l[1][1],"lxml")

# print(l)
# print(sendRequest("https://basketball.realgm.com/nba/stats/2018/Averages/Qualified/points/All/desc/2/Regular_Season"))


