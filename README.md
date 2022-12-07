# Rules-Based Chatbot  

This project is a rules-based chatbot that specializes in everyday conversational English with the ability to load in specialization at a later date, and that can associate callable functions with given sentence patterns.

This codebase contains a program that allows a user to engage in a conversation with a computer, which will respond to the user based on keywords and sentence patterns that it has been programmed to recognize. The program uses regular expressions and fuzzy string matching to recognize user input, and it also logs the conversation to a text file.



## Functions

- `mainCall()`: This is the entry point of the program, where the conversation with the user begins.
- `respond(user_input)`: This function responds to user input by checking for keywords in the user's input and returning a pre-defined response.
- `fuzzyAggregate(phraseA, phraseB, printme=False)`: This function calculates a fuzzy match score for two phrases, using three different fuzzy string matching algorithms. The function returns the average of the three scores.
- `match_sentence_pattern(user_input, patternDict, fuzzSensitivity=80)`: This function matches the user's input against a dictionary of sentence patterns and their associated responses and functions. The function returns the associated responses and function if a match is found, or `None` if no match is found.
- `returnAssociatedMatch(user_input, patternDict)`: This function calls the `match_sentence_pattern` function to match the user's input against the sentence patterns, and then returns the associated responses and function.
- `log_conversation(time, speaker_name, dialogue)`: This function logs the conversation to a text file, including the time, speaker name, and dialogue.

## Usage

To use the program, run the `mainCall()` function. The program will then prompt the user for input and respond based on the user's input.

## Logging Conversations  

The chatbot also includes a function for logging new conversations, including the time, speaker's name, and dialogue for each response and answer. This function can be called each time the chatbot has a new conversation with a user.

```python
def log_conversation(speaker, dialogue):
timestamp = datetime.now()
log_entry = f"{timestamp} - {speaker}: {dialogue}"
with open('conversation_log.txt', 'a') as log_file:
log_file.write(log_entry)
```  
