from translate import Translator
import speech_recognition as sr

r = sr.Recognizer()

try:

    with sr.Microphone() as source2:
        print("Listening")
        r.adjust_for_ambient_noise(source2, duration=0.2)
        audio2 = r.listen(source2)
        MyText = r.recognize_google(audio2)
        print(MyText)
except:

    print("Network Error Occured")

translator = Translator(to_lang="french")
translation = translator.translate(MyText)
print(translation)
