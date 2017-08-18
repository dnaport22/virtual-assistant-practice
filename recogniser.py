import speech_recognition as sr
from requests import Requests
from features.intentSystemList import intentSystemList
from features.dodgybot import main
import yaml
import os

class Recogniser(sr.Recognizer, sr.Microphone, Requests, intentSystemList):
	def __init__ (self):
		self.recogniser = sr.Recognizer()
		self.microphone = sr.Microphone()
		self.request = Requests()
		self.intentList = intentSystemList()
		self.audio = None
		self.response = None
		self.answer = None

	def listen(self, listen_freq=0):
		while listen_freq == 0:
			with self.microphone as source:
				print self.intentList.systemList()
				os.system("say 'here is a list of things i can do for you'")
				os.system("say 'how can i help you'")
				self.audio = self.recogniser.listen(source)

			return True

	def recogniseAudio(self):
		print 'Recognising...'
		self.response = self.recogniser.recognize_google(self.audio)

		return self.response

	def understandResponse(self):
		text = self.response.lower()
		text = text.split(' ')

		question_list = ['how', 'what', 'where']
		task_list = ['generate', 'do', 'create']

		if text[0] == 'open':
			self.answer = self.request.runTask(text[1:])
		elif text[0] == 'search':
			self.answer = self.request.webSearch(text[1:])
		elif text[0] in question_list:
			print self.response
			self.answer = self.request.questionAnalyser(text[0:])
		elif text[0] in task_list:
			self.answer = self.request.taskAnalyser(text[0:])
		elif text[0] == 'chat':
			os.system('cd features/dodgybot && python main.py chat')
		elif text[0] == 'talk':
			os.system('cd features/dodgybot && python main.py talk')

	def say(self):
		if self.answer != None:
			print self.answer
			return os.system("say '%s'"%(self.answer))
		pass



x = Recogniser()
x.listen()
x.recogniseAudio()
x.understandResponse()
x.say()