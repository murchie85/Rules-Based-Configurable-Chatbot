#import necessary libraries
import re
import random
from specialisationObject import *

patternDict = specializationDict

#define a function to respond to user input
def respond(user_input):
	#define a list of keywords
	keywords = ["hello", "hi", "greetings", "hey"]
	#define a list of responses
	responses = ["Hi there!", "Greetings!", "Hello!", "Hey there!"]
	#check if user input contains any of the keywords
	for word in keywords:
		if word in user_input:
			#return a random response from the list of responses
			return random.choice(responses)


#define a function to match user input with sentence patterns
def match_sentence_pattern(user_input,patternDict):
	#loop through the sentence patterns and associated functions
	for topic in patternDict:
		values = patternDict[topic]
		
		#check if the user input matches the sentence pattern
		for sentence in values['patterns']:
			# Compile a regular expression that will match the sentence, ignoringcase and punctuation
			regex = re.compile(f"^{re.escape(user_input)}$", re.IGNORECASE)
			if regex.match(sentence):
				#return the associated function
				return values['responses'],values['function']


#define a function to call the associated function
def call_associated_function(user_input,patternDict):
	#match the user input with the sentence patterns
	associated_responses, associated_function = match_sentence_pattern(user_input,patternDict)
	print(associated_responses)
	print("Calling " + str(associated_function))

	#call the associated function
	#associated_function()

def log_conversation(time, speaker_name, dialogue):
	log_file = open("conversation_log.txt", "a")
	log_file.write("Time: " + time + "\n")
	log_file.write("Speaker: " + speaker_name + "\n")
	log_file.write("Dialogue: " + dialogue + "\n\n")
	log_file.close()



userprompt = input("Hi say something.")
call_associated_function(userprompt,patternDict)
