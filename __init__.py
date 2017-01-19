from fbGroup import FBGroup
from urlToFile import URLToFile
import json


"""
if __name__ == '__main__':
	u = URLToFile()

	file = "test.html"
	#u.urlToFile("https://www.facebook.com/groups/617704971719415/members/", file)
	
	f = FBGroup(file)
	f.getTable()
	
	liste = [{"lien": f.getLink(), "photo": f.getPictures(), "date": f.getDate(), "etudes": f.getStudies() in zip(f.getLink(), f.getPictures(), f.getDate(), f.getStudies())}]
	#print(json.dumps(liste))
	l = []

	for i in range(0, len(f.getLink())):
		d = {}

		lien = f.getLink()[i]
		photo = f.getPictures()[i]
		date = f.getDate()[i]
		etudes = f.getStudies()[i]

		d['lien'] = lien
		d['photo'] = photo
		d['date'] = date
		d['etudes'] = etudes

		l.append(d)
	
	print(json.dumps(l))
"""
if __name__ == '__main__':
	f = FBGroup("toast.html")
	print(f.getPhotoFromLink("toast.html"))