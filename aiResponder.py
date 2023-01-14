#!/usr/bin/env python3

import openai as ai
from sys import argv
import json

with open('my_credentials') as cred:
	ai.api_key = json.loads(cred.read())['openai_api_key']

"""
response = ai.Completion.create(
	model="text-davinci-001",
	prompt="Write a tagline for an ice cream shop.",
	temperature=0.4,
	max_tokens=64,
	top_p=1,
	frequency_penalty=0,
	presence_penalty=0)
"""

def respond_from_ai(prompty:str):
	response = ai.Completion.create(
		model="text-davinci-001",
		prompt = prompty,
		temperature=0.6,
		max_tokens=64,
		top_p=1,
		frequency_penalty=0,
		presence_penalty=0)
	print(response['choices'][0]['text'])
	return response

def main(): respond_from_ai(argv[1])

if __name__ == "__main__": main()
