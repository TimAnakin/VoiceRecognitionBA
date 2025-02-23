from NLP.IntentPredictor import IntentPredictor
from voice_recognition.google_SST import speech_to_text

import keyboard
import sys
from RealtimeSTT import AudioToTextRecorder
import pyautogui
import keyboard
import re

# Variable, um den erkannten Text zu speichern
recognized_text = ""


def process_text(text):
    global recognized_text  
    recognized_text = re.sub(r'[^\w\s]', '', text).lower()  
    print("Erkannter Text :", recognized_text)
    





if __name__ == '__main__':
    # intent_handler = IntentHandler()  # Initialisiere IntentHandler
    predictor = IntentPredictor(confidence_threshold=0.6)
    recorder = AudioToTextRecorder(language="de", input_device_index=1)

    print("Drücke 'f', um die Spracherkennung zu starten. Drücke 'k', um das Programm zu beenden.")

    while True:
        if keyboard.is_pressed("k"):
            print("Programm wird beendet...")
            sys.exit()

        if keyboard.is_pressed("f"):
            print("Spracherkennung gestartet...")
            recorder.text(process_text) 

            if recognized_text:
                print(f"Erkannter Befehl: {recognized_text}")
                intent, probability = predictor.predict(recognized_text)
                
                print(f"Vorhergesagter Intent: {intent} mit Wahrscheinlichkeit: {probability:.4f}")

                if probability < 0.6:
                    print("Ich konnte den Befehl nicht genau zuordnen.")
                else:
                    # result = intent_handler.handle_intent(intent)
                    # print(f"Ergebnis: {result}")
                    pass
            elif recognized_text == None:
                print("Kein verständlicher Sprachbefehl erkannt.")
            recognized_text = "";

