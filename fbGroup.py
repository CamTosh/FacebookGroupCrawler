import json
from bs4 import BeautifulSoup

class FBGroup(object):

	def __init__(self, file):
		file = open(file, encoding='utf8')
		self.soup = BeautifulSoup(file, "html.parser")

	def getCard(self):
		card = self.soup.findAll("td", {"class" : "_51m- vTop hLeft pam"}) # 1 td / profil
		return card

	def getNom(self):
		nom = self.soup.findAll("a", {"id" : "js_1mf"}) # à terminer
		return nom

	def getLiens(self):
		liens = self.soup.findAll("a", {"class" : "_8o _8r lfloat _ohe"}, href=True) # list['href']
		l = [l['href'] for l in liens]
		return l

	def getPhotos(self):
		photos = self.soup.findAll("img", {"class" : "_s0 _rv img"}, src=True) # list['src']
		l = [p['src'] for p in photos]
		return l

	def getEtudes(self):
		etudes = self.soup.findAll("div", {"class" : "_17tq"})
		l = [e.get_text() for e in etudes]
		return l

	def getDate(self):
		dates = self.soup.findAll("abbr") # list ['data-utime']
		l = [d['data-utime'] for d in dates]
		return l

	def createJson(self):
		liste = [{'lien': self.getLiens(),
				  'photo': self.getPhotos(),
				  'etudes': self.getEtudes(),
				  "date": self.getDate()} for liens, photos, etudes, date in zip(self.getLiens(), self.getPhotos(), self.getEtudes(), self.getDate())]
		
		return json.dumps(liste)
