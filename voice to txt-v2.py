import speech_recognition as sr
import pyaudio

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Pls Start your Speech!")
    audio = r.listen(source,timeout=10,phrase_time_limit=100)
print('''*********************************************************
 Convert into the text by selecting the Language
*********************************************************''')
for lang in ["1. English", "2. Hindi","3. French","4. Urdu","5. Exit"]:
    print(lang)
select_lang=int(input("Enter the number>>"))

if select_lang==1:
    try:
        print("Text:"+r.recognize_google(audio))
    except:
        pass
elif select_lang==2:
    try:
        print("Text:"+r.recognize_google(audio, language = 'hi-IN'))
    except:
        pass

elif select_lang==3:
    try:
        print("Text:"+r.recognize_google(audio, language ="fr-FR"))
    except:
        pass
    
elif select_lang==4:
    try:
        print("Text:"+r.recognize_google(audio, language = 'ur-PK'))
    except:
        pass
    
elif select_lang==5:
    print("Have a Good Day")


