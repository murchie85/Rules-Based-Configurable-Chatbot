#import necessary libraries
import re
import random
from specialisationObject import *
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

patternDict = specializationDict




# ENTRY POINT 

def mainCall():
	exit = False
	userprompt = input("Hello. \n")
	while not exit:
		associated_responses, associated_function = returnAssociatedMatch(userprompt,patternDict)
		if(associated_responses!=None):
			print(random.choice(associated_responses))

		print('\n')

		# GET USER INPUT
		userprompt = input("")


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





def fuzzyAggregate(phraseA, phraseB,printme=False):
    fuzzRatio   = fuzz.ratio(phraseA,phraseB)
    fuzzPartial = fuzz.partial_ratio(phraseA,phraseB)
    fuzzToken   = fuzz.token_sort_ratio(phraseA,phraseB)

    fuzzyAggregate = round((fuzzRatio +fuzzPartial + fuzzToken)/3)

    if(printme):
        print('Checking phrases: [' + str(phraseB) + '] , [' + str(phraseA) + ']' + str(fuzzRatio),str(fuzzPartial),str(fuzzToken),str(fuzzyAggregate))


    return(fuzzyAggregate)


#define a function to match user input with sentence patterns
def match_sentence_pattern(user_input,patternDict,fuzzSensitivity=80):
	#loop through the sentence patterns and associated functions
	for topic in patternDict:
		values = patternDict[topic]
		
		#check if the user input matches the sentence pattern
		for sentence in values['patterns']:
			# Compile a regular expression that will match the sentence, ignoringcase and punctuation
			regex = re.compile(f"^{re.escape(user_input)}$", re.IGNORECASE)
			fuzzRatio = fuzzyAggregate(user_input.lower(), sentence.lower()) 
			

			# LOOKING FOR CLOSE MATCH 
			if regex.match(sentence):
				#return the associated responses and function
				return values['responses'],values['function']
			# LOOKING FOR FUZZY MATCH 
			elif(fuzzRatio> fuzzSensitivity):
				#return the associated responses and function
				return values['responses'],values['function']

	return None,None


#define a function to call the associated function
def returnAssociatedMatch(user_input,patternDict):
	#match the user input with the sentence patterns
	associated_responses, associated_function = match_sentence_pattern(user_input,patternDict)
	return(associated_responses, associated_function)

	#call the associated function
	#associated_function()

def log_conversation(time, speaker_name, dialogue):
	log_file = open("conversation_log.txt", "a")
	log_file.write("Time: " + time + "\n")
	log_file.write("Speaker: " + speaker_name + "\n")
	log_file.write("Dialogue: " + dialogue + "\n\n")
	log_file.close()







mainCall()