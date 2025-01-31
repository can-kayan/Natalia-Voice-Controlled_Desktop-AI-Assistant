import speech_recognition as sr
import pyttsx3
def ses_al():
    r = sr.Recognizer()
    print("dinleniyor...")
    with sr.Microphone() as source:
        try:
            ses = r.listen(source)
            komut = r.recognize_google(ses, language="tr-TR") 
            return komut
        except sr.UnknownValueError:
            return ""
        except sr.RequestError:
            return "" 

def sesli_cevap(veri): 
    karakter_map = {
        "ç": "c",
        "ğ": "g",
        "ı": "i",
        "ö": "o",
        "ş": "s",
        "ü": "u",
        "Ç": "C",
        "Ğ": "G",
        "İ": "I",
        "Ö": "O",
        "Ş": "S",
        "Ü": "U",
    }
     
    for turkce, ingilizce in karakter_map.items():
        veri = veri.replace(turkce, ingilizce)
     
    engine = pyttsx3.init()
    sesler = engine.getProperty('voices')
     
    for idx, ses in enumerate(sesler):
        print(f"Ses {idx}: {ses.name} - {ses.languages}") 
     
    engine.setProperty("voice", sesler[0].id)
     
    engine.say(veri)
    engine.runAndWait()
  
