from gtts import gTTS
mytext ="In a world where you can be anything, be kind." #You can give your own test here
language='en'
obj =gTTS(text=mytext,lang=language,slow=False)
obj.save("Quote.mp3")
