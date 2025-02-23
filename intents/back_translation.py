import json
from googletrans import Translator

# Die Daten aus einer JSON-Datei laden
with open('C:/Users/Tim/Desktop/VoiceRecognitionTimSuelz/intents/base_model_advanced.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Translator-Instanz erstellen
translator = Translator()

def back_translate(phrases, target_lang='en'):
    translated_phrases = []
    for phrase in phrases:
        # Zuerst in die Zielsprache (z.B. Englisch) übersetzen
        translation = translator.translate(phrase, dest=target_lang)
        # Dann zurück in die Ausgangssprache (Deutsch) übersetzen
        back_translation = translator.translate(translation.text, dest='de')
        translated_phrases.append(back_translation.text)
    return translated_phrases

# Beispiel-Back-Translation anwenden
augmented_data = {}

for key, phrases in data.items():
    augmented_phrases = back_translate(phrases, target_lang='en')
    print(1)
    augmented_data[key] = phrases + augmented_phrases  # Original und augmentierte Phrasen zusammenführen

# Die erweiterte JSON-Datei speichern
with open('augmented_data.json', 'w', encoding='utf-8') as file:
    json.dump(augmented_data, file, ensure_ascii=False, indent=4)

print("Die augmentierte JSON-Datei wurde gespeichert.")
