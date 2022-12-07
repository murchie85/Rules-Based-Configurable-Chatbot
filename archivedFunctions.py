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

