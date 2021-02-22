# Import the Gtts module for text  
# to speech conversion 
from gtts import gTTS 
  
# import Os module to start the audio file
import os 

fh = open("samples/txt_en.txt", "r")
myText = fh.read().replace("\n", " ")

# Language we want to use 
language = 'en'

output = gTTS(text=myText, lang=language, slow=False)

output.save("output_en_txt.mp3")
fh.close()



###############################
#ARABIC TEXT
###############################

  
fh = open("samples/txt_ar.txt", "r")
myText = fh.read().replace("\n", " ")

# Language we want to use 
language = 'ar'

output = gTTS(text=myText, lang=language, slow=False)

output.save("output_ar_txt.mp3")
fh.close()
