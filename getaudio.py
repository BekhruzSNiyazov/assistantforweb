import SpeechRecognition as sr

def getaudio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(f"You: {said}")
        except Exception as e:
            print("Exception: " + str(e))
    try:
        return said
    except:
        return ""
