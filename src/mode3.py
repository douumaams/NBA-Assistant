import requests
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
			row.append(th.text)
	
	returnValue.append(list(row))
	# Ensuite on récupere les informations sur les joueurs
	row[:] = []
	
	for table in soup.findAll("table"):
		for td in table.findAll("td"):
			row.append(td.text)
		returnValue.append(list(row))
		row[:] = []

	return returnValue

# def loadData(url):
	




l = sendRequest("https://en.wikipedia.org/wiki/Boston_Celtics")
# l = sendRequest("https://basketball.realgm.com/nba/stats/2018/Averages/Qualified/points/All/desc/1/Regular_Season")

# soup = BeautifulSoup(l[1][1],"lxml")

print(l[1][2])
# print(sendRequest("https://basketball.realgm.com/nba/stats/2018/Averages/Qualified/points/All/desc/2/Regular_Season"))


