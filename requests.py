import os
import webbrowser
import operator
from nltk.corpus import stopwords
from features.wordmath import WordMath
from features.qrcodegenrator import QrcodeGenerator

class Requests(WordMath, QrcodeGenerator):
	def __init__ (self):
		self.maths = WordMath()
		self.stop = set(stopwords.words('english'))
		self.maths_operation = None
		self.maths_left = None
		self.maths_right = None
		self.maths_operator_words = {'plus':'+', 'minus':'-', 'multiply':'x'}
		self.maths_operators = {'+':operator.add, '-': operator.sub, 'x':operator.mul}
		self.task_list = ['qr']

	def runTask(self, data):
		for txt in data:
			txt = txt.title()
			os.system("open /Applications/%s*"%(txt))

		return "Opening"

	def webSearch(self, query):
		CHROME_PATH = 'open -a /Applications/Google\ Chrome.app %s'
		txt = '+'.join(query)
		url = "https://www.google.co.uk/search?q={}".format(txt)
		webbrowser.get(CHROME_PATH).open(url)

		return "Searching"

	def taskAnalyser(self, task):
		nlp_words = [i for i in task if i not in self.stop]
		words = ''.join(nlp_words)
		if 'qr' in words:
			os.system("say 'Enter url please'")
			qr_url = input('Enter url please: ')
			qr = QrcodeGenerator([qr_url], text_overlay=True)
			qr.generateQrCode()

			return 'Qr code is generated' 
		else:
			return 'Sorry I am not able to do that'

	def questionAnalyser(self, question):
		nlp_words = [i for i in question if i not in self.stop]
		words = ''.join(nlp_words)
		# print words
		for ops in (self.maths_operators):
			if ops in words:
				self.maths_operation = ops

		self.maths_left = words[0].strip()
		self.maths_right = words[2:].strip()

		# for ops in (self.maths_operator_words):
		# 	if ops in words:
		# 		self.math_operation = ops
		# 		words = words.split(ops)
		# 		self.maths_left = self.maths.textToInteger(words[0].strip())
		# 		self.maths_right = self.maths.textToInteger(words[1].strip())

		return self.mathCalculation()
				

	def mathCalculation(self):
		x = int(self.maths_left)
		y = int(self.maths_right)
		op = self.maths_operators[self.maths_operation]
		return op(x,y)


		

		

