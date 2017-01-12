import json
from bs4 import BeautifulSoup

class FBGroup(object):

	def __init__(self, file):
		file = open(file, encoding='utf8')
		self.soup = BeautifulSoup(file, "html.parser")


	def getTable(self):
		self.table = self.soup.find("table", {"class" : "uiGrid _51mz mtl _5f0n"})

		return self.table


	def getCard(self):
		card = self.table.findAll("td", {"class" : "_51m- vTop hLeft pam"}) # 1 td / profil
		
		return card


	def getName(self):
		name = self.table.findAll("a", {"id" : "js_1mf"}) # à terminer
		
		return name


	def getLink(self):
		link = self.table.findAll("a", {"class" : "_8o _8r lfloat _ohe"}, href=True) # list['href']
		l = [l['href'] for l in link]
		
		return l


	def getPictures(self):
		pictures = self.table.findAll("img", {"class" : "_s0 _rv img"}, src=True) # list['src']
		l = [p['src'] for p in pictures]
		
		return l


	def getStudies(self):
		studies = self.table.findAll("div", {"class" : "_17tq"})
		l = [e.get_text() for e in studies]
		
		return l


	def getDate(self):
		dates = self.table.findAll("abbr") # list ['data-utime']
		l = [d['data-utime'] for d in dates]
		
		return l


	def createJson(self):
		liste = [{'lien': self.getLink(),
				  'photo': self.getPictures(),
				  'studies': self.getStudies(),
				  "date": self.getDate()} for link, pictures, studies, date in zip(self.getLink(), self.getPictures(), self.getStudies(), self.getDate())]
		
		
		return json.dumps(liste)

