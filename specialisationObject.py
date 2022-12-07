specializationDict = {
'greeting': {
'patterns': ['Hi', 'Hello', 'Hey', 'Howdy'],
'responses': ['Hi there!', 'Hello!', 'Hey there!', 'Greetings!'],
'function': 'greeting'
},
'goodbye': {
'patterns': ['Bye', 'Goodbye', 'See ya'],
'responses': ['Goodbye!', 'See you later!', 'Take care!'],
'function': 'goodbye'
},
'weather': {
'patterns': ['What is the weather like?', 'What is the forecast?', 'Is it raining?', 'What is the temperature?'],
'responses': ['It is sunny today!', 'It is cloudy with a chance of rain.', 'It is currently raining.', 'The temperature is {temperature} degrees.'],
'function': 'weather'
},
'time': {
'patterns': ['What time is it?', 'What is the time?', 'What is the hour?', 'What is the minute?'],
'responses': ['It is currently {time}.', 'The time is {time}.', 'The hour is {hour}.', 'The minute is {minute}.'],
'function': 'time'
},
'location': {
'patterns': ['Where are you?', 'Where am I?', 'What is your location?', 'What is my location?'],
'responses': ['I am a chatbot and do not have a physical location.', 'You are currently using me from {location}.', 'I am not sure of your location, please provide it.', 'Your location is {location}.'],
'function': 'location'
},
'age': {
'patterns': ['How old are you?', 'What is your age?', 'When were you born?'],
'responses': ['I am a chatbot and do not have an age.', 'I was created recently and do not have an age.', 'I do not have a birthdate, I am a program.'],
'function': 'age'
},
'movies': {
'patterns': ['What are some good movies?', 'What movies do you recommend?', 'What is a popular movie?'],
'responses': ['Some popular movies are The Godfather, The Shawshank Redemption, and Pulp Fiction.', 'I recommend checking out the IMDB top rated movies for some great suggestions.', 'A popular movie right now is Avengers: Endgame.'],
'function': 'movies'
},
'books': {
'patterns': ['What are some good books?', 'What books do you recommend?', 'What is a popular book?'],
'responses': ['Some popular books are The Alchemist, To Kill a Mockingbird, and 1984.', 'I recommend checking out the New York Times bestseller list for some great suggestions.', 'A popular book right now is Where the Crawdads Sing.'],
'function': 'books'
},
'music': {
'patterns': ['What are some good songs?', 'What music do you like?', 'What is a popular band?'],
'responses': ['Some popular songs are Sweet Child O\' Mine by Guns N\' Roses, Bohemian Rhapsody by Queen, and Stairway to Heaven by Led Zeppelin.', 'I am a chatbot and do not have personal preferences for music.', 'A popular band right now is The 1975.'],
'function': 'music'
}
}