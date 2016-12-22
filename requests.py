import os
import webbrowser

class Requests():
	def __init__ (self):
		pass

	def runTask(self, data):
		for txt in data:
			txt = txt.title()
			return os.system("open /Applications/%s*"%(txt))

	def webSearch(self, query):
		CHROME_PATH = 'open -a /Applications/Google\ Chrome.app %s'
		txt = '+'.join(query)
		url = "https://www.google.co.uk/search?q={}".format(txt)
		 
		return webbrowser.get(CHROME_PATH).open(url)

		

