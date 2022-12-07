# Rules-Based Chatbot  

This project is a rules-based chatbot that specializes in everyday conversational English with the ability to load in specialization at a later date, and that can associate callable functions with given sentence patterns.

## Specialization File  

The specialization file is a text file that contains a list of sentence patterns and associated functions. Each line in the file should contain a sentence pattern and the name of the function to call when the pattern is matched. For example:

```
What is the weather like? -> weather_function
How is the weather? -> weather_function
```

## Logging Conversations  

The chatbot also includes a function for logging new conversations, including the time, speaker's name, and dialogue for each response and answer. This function can be called each time the chatbot has a new conversation with a user.

```python
def log_conversation(speaker, dialogue):
timestamp = datetime.now()
log_entry = f"{timestamp} - {speaker}: {dialogue}"
with open('conversation_log.txt', 'a') as log_file:
log_file.write(log_entry)
```  

