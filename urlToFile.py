import requests

class URLToFile(object):

	def urlToFile(self, url, file):
		r = requests.get(url)
		f = open(file, "w", encoding='utf8')
		f.write(r.text)
		f.close()
