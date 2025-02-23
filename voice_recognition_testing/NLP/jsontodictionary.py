import json

# Dateinamen der beiden JSON-Dateien
file1 = "C:/Users/Tim/Desktop/VoiceRecognitionTimSuelz/voice_recognition_testing/NLP/intents.json"
file2 = "C:/Users/Tim/Desktop/VoiceRecognitionTimSuelz/voice_recognition_testing/NLP/base_model.json"

# Funktion zum Laden der JSON-Dateien
def load_json(filename):
    try:
        with open(filename, "r", encoding="utf-8") as json_file:
            return json.load(json_file)
    except FileNotFoundError:
        print(f"Datei '{filename}' nicht gefunden. Es wird eine leere Datei angenommen.")
        return {}

# JSON-Dateien laden
intents1 = load_json(file1)
intents2 = load_json(file2)

# Zusammenführen der Intents
merged_intents = intents1.copy()

for intent, sentences in intents2.items():
    if intent in merged_intents:
        merged_intents[intent].extend(sentences)  # Falls Intent existiert, Sätze hinzufügen
    else:
        merged_intents[intent] = sentences  # Falls neuer Intent, hinzufügen

# Aktualisierte JSON-Datei speichern
output_filename = "updated_intents.json"
with open(output_filename, "w", encoding="utf-8") as json_file:
    json.dump(merged_intents, json_file, ensure_ascii=False, indent=4)

print(f"Datei '{output_filename}' wurde erfolgreich erstellt!")
