#!/usr/bin/env python3

import fakeyou, os, json
from sys import argv

with open('my_credentials') as cred:
	login, password = json.loads(cred.read())['fakeyou']

with open('voicecodes.json') as voices:
	voice = json.loads(voices.read())["Vincent Price (Vincent Price)"]

fy=fakeyou.FakeYou()
fy.login(login, password)

def make_a_voice(words):
	try:
		print('fakin it up')
		fy.say(text= words,ttsModelToken = voice[1])
		os.system('aplay fakeyou.wav')
	except fakeyou.exception.TooManyRequests:
		print("Cool down")

def main():
	make_a_voice(argv[1])


if __name__=="__main__": main()
