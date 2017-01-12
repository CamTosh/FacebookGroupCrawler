from fbGroup import FBGroup
from urlToFile import URLToFile

if __name__ == '__main__':
	u = URLToFile()

	file = "test.html"
	u.urlToFile("https://www.facebook.com/groups/617704971719415/members/", file)
	
	f = FBGroup(file)
	print(str(f.getEtudes()))