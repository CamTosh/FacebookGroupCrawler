import requests

class URLToFile(object):

	def urlToFile(self, url, file):
		r = requests.get(url)
		f = open(r.text, "w")
		f.write(r)
		f.close()

		if f.read():
			return True
		else:
			return False
			