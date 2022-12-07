#import necessary libraries
import re
import random
import specializationObject

patternDict = specialization_file

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


# NOT REQUIRED AT THE MOMENT
def load_specialization(specialization_file):
	#open the specialization file
	with open(specialization_file, "r") as f:
	#read the contents of the file
	contents = f.read()
	#split the contents into lines
	lines = contents.split("\n")
	#loop through the lines
	for line in lines:
		#split the line into sentence pattern and associated function
		sentence_pattern, callable_function = line.split("->")
		#associate the sentence pattern with the associated function
		associate_function(sentence_pattern, callable_function)



#define a function to associate callable functions with given sentence patterns
def associate_function(sentence_pattern, callable_function):
	#define a dictionary to store the sentence patterns and associated functions
	sentence_patterns_functions = {}
	#add the sentence pattern and associated function to the dictionary
	sentence_patterns_functions[sentence_pattern] = callable_function
	#return the dictionary
	return sentence_patterns_functions



#define a function to match user input with sentence patterns
def match_sentence_pattern(user_input):
	#loop through the sentence patterns and associated functions
	for sentence_pattern, callable_function in sentence_patterns_functions.items():
	#check if the user input matches the sentence pattern
	if re.match(sentence_pattern, user_input):
	#return the associated function
	return callable_function

#define a function to call the associated function
def call_associated_function(user_input):
	#match the user input with the sentence patterns
	associated_function = match_sentence_pattern(user_input)
	#call the associated function
	associated_function()

def log_conversation(time, speaker_name, dialogue):
	log_file = open("conversation_log.txt", "a")
	log_file.write("Time: " + time + "\n")
	log_file.write("Speaker: " + speaker_name + "\n")
	log_file.write("Dialogue: " + dialogue + "\n\n")
	log_file.close()


