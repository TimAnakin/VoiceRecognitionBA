import difflib
import csv
import re
import numpy as np
from RealtimeSTT import AudioToTextRecorder
import pyautogui
import keyboard
import json
from NLP.IntentPredictor import IntentPredictor

test_sentences = {
    # Deine Sätze hier...
    "arbeitsmodus": [
        "Aktiviere den Arbeitsmodus",
        "Ich möchte den Arbeitsmodus starten",
        "Starte bitte den Arbeitsmodus",
        "Der Arbeitsmodus soll gestartet werden",
        "Aktiviere bitte den Arbeitsmodus"
    ],
    "check_count_große_schraube": [
        "Wie viele große Schrauben sind vorhanden?",
        "Überprüfe wie viele große Schrauben noch vorhanden sind",
        "Ich will wissen wie viele große Schrauben noch da sind",
        "Gib mir die Anzahl an großen Schrauben",
        "Ich möchte die Anzahl an großen Schrauben erfahren"
    ],
    "check_count_kleine_schraube": [
        "Wie viele kleine Schrauben gibt es?",
        "Überprüfe wie viele kleine Schrauben noch vorhanden sind",
        "Sind noch kleine Schrauben vorhanden?",
        "Gib mir die Anzahl an kleinen Schrauben",
        "Wie viele kleine Schraube sind noch vorhanden"
    ],
    "check_count_oberteil": [
        "Überprüfe die Anzahl an Oberteilen",
        "Wie viele Oberteile sind da",
        "Wie viele Oberteile hast du noch",
        "Gib mir die Anzahl an vorhandenen Oberteilen",
        "Wie viele Oberteile gibt es noch"
    ],
    "check_count_spitze": [
        "Wie viele Spitzen hast du noch",
        "Welche Anzahl an Spitzen sind noch da",
        "Gib mir die Anzahl an vorhandenen Unterteilen",
        "Wie viele Unterteile sind noch da",
        "Checke wie viele Unterteile noch vorhanden sind"
    ],
    "check_griff": [
        "Prüfe ob der Griff da ist",
        "Sind noch Griffe da",
        "Hast du noch Griffe",
        "Ist noch ein Griff vorhanden",
        "Hast du noch Oberteile"
    ],
    "check_große_schraube": [
        "Gibt es noch große Schrauben",
        "Sind noch große Schrauben vorhanden?",
        "Hast du noch große Schrauben",
        "Checke ob noch große Schrauben vorhanden sind",
        "Ich möchte wissen ob es noch große Schrauben gibt"
    ],
    "check_kleine_schraube": [
        "Sind noch kleine Schrauben vorhanden?",
        "Wie viele kleine Schrauben sind noch übrig?",
        "Gibt es noch kleine Schrauben?",
        "Überprüfe, wie viele kleine Schrauben noch da sind",
        "Gib mir die Anzahl an kleinen Schrauben"
    ],
    "check_spitze": [
        "Ist noch eine Spitze da",
        "Prüfe ob es noch Unterteile gibt",
        "Gibt es noch Spitzen?",
        "Sind noch Spitzen vorhanden",
        "Hast du noch Spitzen?"
    ],
    "drop_all": [
        "Platziere alle Objekte in die Halterung",
        "Mach einmal alle Schritte",
        "Starte einen Durchlauf",
        "Platziere alle Teile in die Halterung",
        "Füge alle Teile in die Halterung"
    ],
    "drop_griff": [
        "Setze den Griff in die Halterung",
        "Kannst du den Griff in die Halterung setzen",
        "Platziere bitte den Griff in die Halterung",
        "Pack den Griff in die Mitte",
        "Ich möchte das du den Griff in die Halterung setzt"
    ],
    "drop_große_schraube": [
        "Packe die große Schraube in die Halterung",
        "Platziere die große Schraube in die Halterung",
        "Setze bitte die große Schraube in die Halterung",
        "Packe die große Schraube in die Mitte",
        "Bitte platziere die große Schraube in die Halterung"
    ],
    "drop_kleine_schraube": [
        "Packe die kleine Schraube in die Halterung",
        "Platziere die kleine Schraube in die Halterung",
        "Setze die kleine Schraube in die Halterung",
        "Ich möchte dass du die kleine Schraube in die Halterung packst",
        "Ich will dass du die kleine Schraube in die Halterung setzt"
    ],
    "drop_spitze": [
        "Packe die Spitze in die Halterung",
        "Ich möchte das du die Spitze in die Mitte setzt",
        "Platziere die Spitze in die Halterung",
        "Setze die Spitze in die Halterung",
        "Ich will das du die Spitze in die Halterung platzierst"
    ],
    "give_griff": [
        "Ich möchte den Griff haben",
        "Gib mir den Griff",
        "Reich mir den Griff",
        "Ich will den Griff haben",
        "Ich möchte bitte den Griff haben"
    ],
    "give_große_schraube": [
        "Ich will das du mir eine große Schraube gibst",
        "Gib mir die große Schraube",
        "Ich will die große Schraube haben",
        "Könntest du mir die große Schraube geben",
        "Reich mir die große Schraube"
    ],
    "give_kleine_schraube": [
        "Ich brauche noch eine kleine Schraube",
        "Ich benötige eine kleine Schraube",
        "Reich mir die kleine Schraube",
        "Gib mir eine kleine Schraube",
        "Ich will eine kleine Schraube haben"
    ],
    "give_tip_or_bottom": [
        "Ich würde gerne das Unterteil haben",
        "Bitte gib mir die Spitze",
        "Gib mir das Unterteil",
        "Ich möchte die Spitze haben",
        "Kannst du mir bitte die Spitze geben"
    ],
    "open_linken_greifer": [
        "Öffne bitte den linken Greifer",
        "Ich möchte das du den linken Greifer öffnest",
        "Öffne den linken Greifer",
        "Lass das linke Objekt los",
        "Lass links los"
    ],
    "open_rechten_greifer": [
        "Öffne die rechte Seite",
        "Öffne den rechten Greifer",
        "Ich möchte das du den rechten Greifer öffnest",
        "Kannst du den rechten Greifer öffnen",
        "Lass rechts los"
    ],
    "do_next_step": [
        "Durchführe den nächsten Schritt",
        "Ich will das du weiter machst",
        "Mache den nächsten Schritt",
        "Führe den nächsten Schritt aus",
        "Mach weiter"
    ],
    "offener_modus": [
        "Aktiviere den offenen Modus",
        "Würdest du den offenen Modus starten",
        "Starte den offenen Modus",
        "Ich möchte das du den offenen Modus startest",
        "Aktiviere den offenen Modus"
    ],
    "start_application": [
        "Starte die Applikation",
        "Starte die Anwendung.",
        "Start",
        "Beginne mit der Anwendung",
        "Starten"
    ],
    "stop_application": [
        "Stoppe die Anwendung",
        "Stop",
        "Beende die Applikation",
        "Schließe die Applikation",
        "Beende die Anwendung"
    ],
    "tell_next_step": [
        "Was ist der nächste Schritt",
        "Was muss ich als nächstes machen",
        "Wie gehe ich vor",
        "Was muss ich tun",
        "Wie funktioniert der nächste Schritt"
    ]
}






recognized_text = ""
all_sentences = [sentence for sentences in test_sentences.values() for sentence in sentences]
current_index = 0
predictor =IntentPredictor()
intents_dict = {}

def add_sentence(intent, sentence):
    """Fügt einen Satz zu einem Intent in intents_dict hinzu."""
    if intent not in intents_dict:
        intents_dict[intent] = []  # Falls der Intent noch nicht existiert, erstelle eine neue Liste
    intents_dict[intent].append(sentence) 
def save_dict_to_json(dictionary, filename="intents.json"):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(dictionary, file, ensure_ascii=False, indent=4)



def clean_text(text):
    """Bereinigt den Text von Satzzeichen."""
    return re.sub(r"[.,!?]", "", text)
def find_intent_for_expected_sentence(expected_sentence):
    """Finde den Intent basierend auf dem erwarteten Satz."""
    for intent, sentences in test_sentences.items():
        if expected_sentence in sentences:
            return intent
def process_text(text):
    """Verarbeitet den erkannten Text und vergleicht ihn mit den Test-Sätzen."""
    global recognized_text, current_index
    recognized_text = clean_text(text)
    print("Erkannter Text:", recognized_text)
    
    # Vergleich des erkannten Textes mit dem nächsten erwarteten Satz
    best_match, best_ratio, best_levenshtein, levenshtein_ratio_value,wer, word_accuracy, position_accuracy, end_accuracy,predicted_intent,probality = compare_text(recognized_text)
    expected_sentence = all_sentences[current_index]
    intent = find_intent_for_expected_sentence(expected_sentence)
    if end_accuracy > 65:
        add_sentence(intent,recognized_text)
  
    save_dict_to_json(intents_dict)
    # Speichern der Ergebnisse
    save_results(recognized_text, best_match, best_ratio, best_levenshtein,round(levenshtein_ratio_value*100,2),wer, word_accuracy, position_accuracy, end_accuracy,intent,predicted_intent,probality)
    
    # Nächsten Satz ausgeben
    current_index = (current_index + 1) % len(all_sentences)
    print("Als nächstes zu sprechen:", all_sentences[current_index])

def levenshtein_distance(str1, str2):
    """Berechnet die Levenshtein-Distanz zwischen zwei Strings."""
    n, m = len(str1), len(str2)
    dp = np.zeros((n+1, m+1))
    for i in range(n+1):
        for j in range(m+1):
            if i == 0: dp[i][j] = j
            elif j == 0: dp[i][j] = i
            else:
                dp[i][j] = min(dp[i-1][j-1] + (str1[i-1] != str2[j-1]),
                               dp[i][j-1] + 1, dp[i-1][j] + 1)
    return dp[n][m]
def word_error_rate(reference, hypothesis):
    """Berechnet die Word Error Rate (WER) basierend auf der Levenshtein-Distanz."""
    ref_words = reference.split()
    hyp_words = hypothesis.split()
    
    levenshtein_dist = levenshtein_distance(ref_words, hyp_words)
    
    return levenshtein_dist / len(ref_words) if len(ref_words) > 0 else 0

def levenshtein_ratio(str1, str2):
    levenshtein_dist = levenshtein_distance(str1, str2)
    max_len =  len(str2);
    ratio = ( levenshtein_dist / max_len)  if max_len > 0 else 0
    return ratio


def string_accuracy(word1: str, word2: str, penalty_distance ,penalty_length) -> float:
        len1, len2 = len(word1), len(word2)
        max_len = max(len1, len2)
        match_count= 0
        extra_chars_penalty = 0
        total_penalty = 0
        used_indices = set()  # Set zum Speichern der bereits verwendeten Indizes

        for i in range(len1):
            for j in range(len2):
                # Wenn der Buchstabe an der richtigen Position und noch nicht verwendet wurde
                if word1[i] == word2[j] and i == j and i not in used_indices:
                    print(word1[i], j, i)
                    match_count += 1
                    used_indices.add(i)  # Markiere den Index als verwendet
                    break  # Weiter mit dem nächsten i, innerer Loop wird abgebrochen
                # Wenn der Buchstabe übereinstimmt, aber nicht an der richtigen Position
                elif word1[i] == word2[j] and j not in used_indices:
                    distance = abs(i - j)
                    penalty = (distance * penalty_distance) / max_len  # Je weiter entfernt, desto höher die Strafe
                    total_penalty += penalty
                    match_count += 1
                    used_indices.add(j)  # Markiere den Index j als verwendet
                    break  # Wei
        if len1 != len2 :
            extra_chars_penalty = ((abs(len1 - len2) ** penalty_length) / max_len) 

        accuracy = ((match_count- total_penalty-extra_chars_penalty) / max_len) * 100  # Basisgenauigkeit
        return max(accuracy, 0)
def calculate_accuracy(input, expected, alpha=2):
    """Berechnet Wort- und Positionsgenauigkeit zwischen zwei Sätzen."""
    input = input.lower().split()
    abs_pos = get_word_positions(expected)
    expected = expected.lower().split()
    predicted_list = []
    word_accuracy_score = 0.0
    total_words = max(len(input), len(expected))  # Statt `total_words_detected_string`
    
    for word in input:
        best_accuracy = 0
        best_match = "xxx"  # Standardwert für kein gutes Match
        
        for expected_word in expected:
            current_accuracy = string_accuracy(word, expected_word, 1.3, 2.2)
            if current_accuracy > best_accuracy:
                best_accuracy = current_accuracy
                best_match = expected_word  # Speichere das beste erwartete Wort
        
        if best_accuracy >= 40:
            word_accuracy_score += best_accuracy
            predicted_list.append(best_match)  # Jetzt wird das beste Wort gespeichert
        else:
            predicted_list.append("xxx")

    print(predicted_list)
    score = 0
    for index, word in enumerate(predicted_list):
        if word == "xxx":
            continue
        for correct_word, positions in abs_pos:
            print(word)
            print(correct_word)
            if word == correct_word:
                print(1)
                min_distance = min(abs(index - pos) for pos in positions)
                score += max(0, (1 - (min_distance / total_words)) * 100)
                break

    word_accuracy = (word_accuracy_score / total_words) if total_words > 0 else 0
    position_accuracy = (score / total_words) if total_words > 0 else 0
    end_accuracy = (position_accuracy + word_accuracy) / 2
    return word_accuracy, position_accuracy, end_accuracy

def predictionAnalysisforBert(input):
      label,probabality = predictor.predict(input)
      return label, probabality;


    

def get_word_positions(sentence: str):
    words = sentence.lower().split()
    word_positions = {}
    
    for index, word in enumerate(words):
        if word in word_positions:
            word_positions[word].append(index)
        else:
            word_positions[word] = [index]
    
    return [(word, positions) for word, positions in word_positions.items()]


        
        
        
    return 
def compare_text(input_text):
    """Vergleicht den erkannten Text mit dem aktuellen erwarteten Satz."""
    expected_sentence = clean_text(all_sentences[current_index])
    ratio = difflib.SequenceMatcher(None, input_text.lower(), expected_sentence.lower()).ratio()
    levenshtein_dist = levenshtein_distance(input_text.lower(), expected_sentence.lower())
    word_accuracy, position_accuracy, end_accuracy = calculate_accuracy(input_text, expected_sentence)
    levenshtein_ratio_value = levenshtein_ratio(input_text.lower(), expected_sentence.lower())
    print(f"Bester Treffer: {expected_sentence} (Übereinstimmung: {ratio:.2%}, Levenshtein-Distanz: {levenshtein_dist}, Levenshtein-Ratio: {levenshtein_ratio_value:.2%}, Wortgenauigkeit: {word_accuracy:.2f}%, Positionsgenauigkeit: {position_accuracy:.2f}%, Endgenauigkeit: {end_accuracy:.2f}%)")
    label,probality = predictionAnalysisforBert(input_text)
    wer = word_error_rate(expected_sentence, input_text)
    return expected_sentence, ratio, levenshtein_dist,levenshtein_ratio_value,wer, word_accuracy, position_accuracy, end_accuracy,label,probality, 

def save_results(input_text, expected_sentence, best_ratio, best_levenshtein,levenshtein_ratio_value,wer, word_accuracy, position_accuracy, end_accuracy,intent, detected_intent,probabilty):
    """Speichert die Ergebnisse in eine CSV-Datei."""
    with open("sst_results.csv", mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([
            input_text, 
            expected_sentence, 
            f"{best_ratio:.2%}", 
            best_levenshtein, 
           levenshtein_ratio_value,
            f"{word_accuracy:.2f}%", 
            f"{position_accuracy:.2f}%", 
            f"{end_accuracy:.2f}%",
            intent,
            detected_intent,
            f"{probabilty*100:.2f}%",
        ])

if __name__ == '__main__':
    string2 = "überprüren die musik musik evaluieren "
    string1 = "überprüren die musi"
    print(calculate_accuracy(string1,string2))
    # print("Wait until it says 'speak now'")
    # recorder = AudioToTextRecorder(language="de", input_device_index=1)

    # # Erstelle die CSV-Datei mit korrektem Header
    # with open("sst_results.csv", mode="w", newline="", encoding="utf-8") as file:
    #     writer = csv.writer(file)
    #     writer.writerow(["Gesprochener Satz", "Erwarteter Satz", "SequenceMatcher Genauigkeit", "Levenshtein-Distanz", "Wortgenauigkeit", "Positionsgenauigkeit", "Endgenauigkeit"])

    # print("Als erstes zu sprechen:", all_sentences[current_index])

    # while True:
    #     if keyboard.is_pressed("f"):
    #         recorder.text(process_text) 
            