import speech_recognition as sr
import keyboard

def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        print("Warte auf Sprachbefehl...")
        recognizer.adjust_for_ambient_noise(source, duration=1)  # Umgebungsgeräusche anpassen
        
        
        try:
            # Hier warten wir etwas länger, um alle möglichen Befehle aufzunehmen
            audio = recognizer.listen(source, timeout=7, phrase_time_limit=5)
            print("Verarbeite...")
            
            # Spracherkennung durchführen
            command = recognizer.recognize_google(audio, language="de-DE")
            print(f"Erkannter Befehl: {command}")
            return command.lower()
        
        except sr.UnknownValueError:
            print("Konnte den Befehl nicht verstehen.")
            return None
        except sr.RequestError as e:
            print(f"Fehler beim Abrufen der Ergebnisse: {e}")
            return None
