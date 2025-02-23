import json
import os

def load_json(file_path):
    """Lädt eine JSON-Datei und gibt den Inhalt zurück."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def merge_sentences(json_files):
    """Fügt die Sätze aus mehreren JSON-Dateien zusammen und sortiert sie."""
    all_sentences = {}

    for file_path in json_files:
        # Lade die JSON-Datei
        data = load_json(file_path)
        
        # Iteriere über alle Header und Sätze
        for header, sentences in data.items():
            if header not in all_sentences:
                all_sentences[header] = []
            
            # Füge die Sätze der jeweiligen Header-Liste hinzu
            all_sentences[header].extend(sentences)
    
    # Sortiere die Sätze in jedem Header alphabetisch
    for header in all_sentences:
        all_sentences[header] = sorted(all_sentences[header])

    return all_sentences

def save_to_json(data, output_file):
    """Speichert die kombinierten und sortierten Daten in einer neuen JSON-Datei."""
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def main():
    # Pfade zu den drei JSON-Dateien (hier musst du die echten Pfade angeben)
    json_files = ["C:/Users/Tim/Desktop/VoiceRecognitionTimSuelz/intents/intents_after_sst.json", "C:/Users/Tim/Desktop/VoiceRecognitionTimSuelz/intents/intents_after_sst_part3.json"]
    
    # Kombinieren und sortieren der Sätze
    combined_data = merge_sentences(json_files)
    
    # Speichern der kombinierten Daten in einer neuen Datei
    save_to_json(combined_data, "combined_sorted_sentences.json")
    
    print("Die Sätze wurden erfolgreich zusammengeführt und sortiert.")

# Hauptprogramm ausführen
if __name__ == "__main__":
    main()
