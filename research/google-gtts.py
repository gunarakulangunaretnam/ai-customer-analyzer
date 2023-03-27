# Importing the gTTS library
from gtts import gTTS
import os

# Tamil text to convert to speech
text = "සුභ සන්ද්යාවක්"

# Language in which you want to convert
language = 'si'

# Passing the text and language to the gTTS module
tts = gTTS(text=text, lang=language)

# Saving the converted audio in a file named welcome.mp3
tts.save("welcome.mp3")
