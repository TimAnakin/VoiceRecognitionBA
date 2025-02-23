from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
from typing import List
import numpy as np
from sklearn.metrics import precision_score, recall_score, f1_score, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

class IntentPredictor:
    def __init__(self, confidence_threshold: float = 0.0):
        self.tokenizer = AutoTokenizer.from_pretrained("./trained_model")
        self.model = AutoModelForSequenceClassification.from_pretrained("./trained_model")
        self.labels = []
        self.confidence_threshold = confidence_threshold
        self.labels = [
    "arbeitsmodus", "check_count_große_schraube", "check_count_kleine_schraube",
    "check_count_oberteil", "check_count_spitze", "check_griff", "check_große_schraube",
    "check_kleine_schraube", "check_spitze", "drop_all", "drop_griff", "drop_große_schraube",
    "drop_kleine_schraube", "drop_spitze", "give_griff", "give_große_schraube", "give_kleine_schraube",
    "give_tip_or_bottom", "open_linken_greifer", "open_rechten_greifer", "do_next_step",
    "offener_modus", "start_application", "stop_application", "tell_next_step", 
]


    def predict(self, text: str):

        # Tokenisierung und Modellvorhersage
        inputs = self.tokenizer(
            text, return_tensors="pt", truncation=True, padding="max_length", max_length=100
        )
        outputs = self.model(**inputs)
        probabilities = torch.nn.functional.softmax(outputs.logits, dim=-1)
        predicted_label_idx = torch.argmax(probabilities).item()
        probability = probabilities[0, predicted_label_idx].item()

        if not self.labels:
            raise ValueError("Labels wurden nicht gesetzt.")
        
        predicted_label = self.labels[predicted_label_idx]
        
        # Confidence-Threshold prüfen
        if probability < self.confidence_threshold:
            return "Unsicher, bitte genauer angeben.", probability
        
        return predicted_label, probability



predictor = IntentPredictor()
test_sentences = {
    "arbeitsmodus": [
        "Aktiviere bitte den Arbeitsmodus",
        "Aktivieren bitte den Arbeitsmuros",
        "Aktivieren den Arbeitsmodus",
        "Aktiviertel den Arbeitsmuros",
        "Bestehrte bitte den Arbeitsmuros",
        "Der Arbeitsmodus soll gestartet werden",
        "Der Arbeitsmuro soll gestartet werden",
        "Der Arbeitsmutter soll gestartet werden",
        "Ich möchte den Arbeitsmodus starten",
        "Ich möchte den Arbeitsmodus starten",
        "Ich möchte den Arbeitsmuro starten",
        "Starte bitte den Arbeitsmodus",
        "Startet bitte den Arbeitsmodus"
    ],
    "check_count_große_schraube": [
        "Gibt mir die Anzahl an großen Schrauben",
        "Gibt mir die anzurein großen Schrauben",
        "Ich möchte die Anzahl an großen Schrauben erfahren",
        "Ich möchte die anzahlen großen Schrauben erfahren",
        "Ich will wissen die für die große Schrauben noch da sind",
        "Ich will wissen die viele große Schrauben noch da sind",
        "Wie viele große Schrauben sind voran",
        "Wie viele große Schrauben sind vorhin",
        "Überprüfe viele große Schrauben noch vorhanden sind"
    ],
    "check_count_kleine_schraube": [
        "Die wird die Ansel an kleinen Schroben",
        "Gibt mir die Anzahl einen kleinen Schroben",
        "Sie sind noch keine Schrauben vorhanden",
        "Sind noch kleine Schrauben vorhanden",
        "Sind noch kleine Schrauben vorhanden",
        "Wie viele kleine Schrauben gibt es",
        "Wie viele kleine Schrauben gibt es",
        "Wie viele kleine Schrauben sind noch da",
        "Wie viele kleine Schrauben sind noch vorhanden",
        "Überprüfe wie viele kleine Schrauben noch vorhanden sind",
        "Überprüfe wir wie viele kleine Schrauben noch vorhanden sind"
    ],
    "check_count_oberteil": [
        "Gehen wir die Anzahl an vorhandenen Oberteilen",
        "Gibt mir die Anzahl an vorhandenen Oberthalen",
        "Wie viele Oateilig gibt es noch",
        "Wie viele Oberteile gibt es noch",
        "Wie viele Oberteile hast du noch",
        "Überprüfe die Anzahl an Oberteilen",
        "Überprüfe die Anzahl an Oberteilen"
    ],
    "check_count_spitze": [
        "Check dir wie viele Unterteile noch vorhanden sind",
        "Check wie viele Unterteile noch vorhanden sind",
        "Gehen wir die Anzahl an vorhandenen Unterteilen",
        "Welche Anze einspitzen sind noch da",
        "Welche Anzeilen Spitzen sind auch da",
        "Wie viele Spitzen hast du noch",
        "Wie viele Spitzen hast du noch",
        "Wie viele Unterteile sind noch da",
        "Wie viele Unterzeides sind auch da"
    ],
    "check_griff": [
        "Hast du noch drüfe",
        "Hast du noch grüffeln",
        "Hast du noch überteile",
        "Hast es noch Oberteile",
        "Ist doch ein Griff vorhanden",
        "Ist noch ein Griff von",
        "Prüfer ob der Griff da ist",
        "Sieht noch guffe da",
        "Sind auch kriffe da",
        "Wir prüfer ob der Griff da ist"
    ],
    "check_große_schraube": [
        "Checker noch große Schrauben vor anden sind",
        "Checker ob noch große Schrauben vorhanden sind",
        "Gibt es noch große Schrauben",
        "Gibt es noch große Schrauben",
        "Hast du noch große Schrauben",
        "Hast du noch große Schrauben",
        "Ich möchte wissen ob es noch große Schrauben gibt",
        "Ich möchte wissen ob es noch große Schrauben gibt",
        "Sind auch große Schrauben von ",
        "Sind noch große Schrauben vorhanden"
    ],
    "check_kleine_schraube": [
        "Gibt es noch kleine Schrauben",
        "Gibt es noch kleine Schroben",
        "Sind noch kllene Schroben da",
        "Hast du noch klone schruben"
    ],
    "check_spitze": [
        "Gibt es noch Spitzen",
        "Gibt es noch Spitzen",
        "Hast du noch Spitzen",
        "Hast du noch Spitzen",
        "Ist noch ein Spitz oder",
        "Ist noch ein Spitze da",
        "Pröfer ob es noch unterteile gibt",
        "Prüfer ob es noch unterteile gibt",
        "Wir sind noch Spitzen vorhanden"
    ],
    "drop_all": [
        "Ach mach einmal alle Schröße",
        "Füge alle Teile in die Halterung",
        "Fügt alle Teile in die Haltrung",
        "Katziere alle Teile in die Halterung",
        "Mach einmal alle Schritte",
        "Platz hier alle teilen die Halterung",
        "Plaziere alle Objekte in die Alterung",
        "Start ein Durchlauf",
        "Start einen Durchlauf"
    ],
    "drop_griff": [
        "Ich möchte das so den Griff in die Halterung setzt",
        "Ich möchte das zu den Griff in die Halterung setzt",
        "Kannst du den Griff in die Halterung setzen",
        "Kannst du den Griff in die Haltruung setzen",
        "Mit Laziere bitte den Griff in die Haltruung",
        "Pack den Griff in die Mitte",
        "Packt den Griff in die Mitte",
        "Platziere bitte den Griff in die Halterung",
        "Setze den Griff in die Halte oben",
        "Sitzte den Griff in die Halterung"
    ],
    "drop_große_schraube": [
        "Besätze bitte die große Schraube in die Halterung",
        "Bitte platziere die große Schraube in die Alterung",
        "Bitte platziere die große Schraube in die Halterung",
        "Packen die große Schraube in die Halterung",
        "Packen die große Schraube in die Halterung",
        "Packen die große Schraube in die Mitte",
        "Packen die große Schraube in die Mitte",
        "Parklarziere die große Schraube in die Alterung",
        "Platziere die größte Schraube in die Halterung",
        "Setze bitte die große Schraube in die Haltrung"
    ],
    "drop_kleine_schraube": [
        "Ich möchte das du die keine Schraube in die Halterung pakt",
        "Ich möchte das so die kleine Schraube in die Halterung pakt",
        "Ich will das du die kleine Schraube in die Halterung setzt",
        "Ich will das du die kleine Schraube in die Halterung setzt",
        "Packet die Keine Schrobe in die Halterung",
        "Packet die kleine Schrobe in die Halterung",
        "Platziere die keine Schraube in die Halterung",
        "Platziere die kleine Schraube in die Haltruung",
        "Sitzte die kleine Schraube in die Halterung",
        "Sätze die kleine Schraube in die Halte rum"
    ],
    "drop_spitze": [
        "Ich möchte das Rischpitze in die Mitte setzt",
        "Ich möchte das zu die Spitze in die Mitte setzt",
        "Ich will das du die Spitze in die Halterung platzierst",
        "Ich will das du die Spitze in die Halterung platzierst",
        "Packen die Spitze in die Halterung",
        "Pake die Spitze in die Alterung",
        "Platziere die Spitze in die Halterung",
        "Plaziere die Spitze in die Halterung",
        "Sätze die Spitze in die Halterung",
        "Sätze die Spitze in die Halterung"
    ],
    "give_griff": [
        "Gibt mir den Griff",
        "Gibt mir den Griff",
        "Ich möchte bitte den Griff haben",
        "Ich möchte den Griff haben",
        "Ich möchte den Griff haben",
        "Ich möchte ein bisschen den Griff haben",
        "Ich will den Griff haben",
        "Ich will den Griff haben",
        "Reich mir den Griff",
        "Reich mit den Griff"
    ],
    "give_große_schraube": [
        "Gibt mir die große Schaube",
        "Ich will das zu mir eine große Schraube gibt",
        "Ich will das zum mir eine große Schraube gibt's",
        "Ich will die große Schaube haben",
        "Ich will die große Schrauber haben",
        "Kann es du mir die große Schraube geben",
        "Kannst du mir die große Schraube geben",
        "Reich mir die große Schraube",
        "Reich mit die große Schraube"
    ],
    "give_kleine_schraube": [
        "Gibt mir eine kleine Schraube",
        "Ich benötige eine kleine Schraube",
        "Ich benötige eine kleine Schrobe",
        "Ich brauche noch eine kleine Schraube",
        "Ich brauche noch eine kleine Schraube",
        "Ich will eine kleine Schaube haben",
        "Ich will eine kleine Schrobe haben",
        "Reich mir die keine Schrobe"
    ],
    "give_tip_or_bottom": [
        "Bitte gehen wir die Spitze",
        "Bitte geht mir die Spitze",
        "Gibt mir das Unterteil",
        "Gibt mir das unterteil",
        "Ich möchte die Spitze haben",
        "Ich möchte die Spitze haben",
        "Ich würde gerne das Unterteil haben",
        "Ich würde gerne das Unterteil haben",
        "Kannst du mir bitte die Spitze geben",
        "Kannst du mir bitte die Spitze geben"
    ],
    "open_linken_greifer": [
        "Ich möchte das zu den Linken greifen veröffn ist",
        "Ich möchte dass du linken greifer öffnest",
        "Las links los",
        "Lass das Linkobjekt los",
        "Lass links los",
        "Lasst das linken Objekt los",
        "Öffne bitte den Link greife",
        "Öffne bitte den Linken greif her",
        "Öffne den linken Greifer",
        "Öfter der Link greifer"
    ],
    "open_rechten_greifer": [
        "Ich möchte das für den rechten Greifer öffnest",
        "Ich möchte das so die rechten greifer öffnest",
        "Lasst rechts los",
        "Öffne den richtigen Kreif vor",
        "Öffne die rechte Seite",
        "Öffne die rechte Seite",
        "Öffte den rechten Gräufer"
    ],
    "do_next_step": [
        "Durch Führ der nächsten Schritt",
        "Durch Schühe den ich will das du weiter machst",
        "Für den nächsten Schritt aus",
        "Ich will das du weitermachst",
        "Mach den nächsten Schritt",
        "Mach er den nächsten Schritt",
        "Mach weiter",
        "Mach weiter",
        "Nächsten Schritt für den nächsten Schritt aus"
    ],
    "offener_modus": [
        "Aktiviere den offenen Modus",
        "Aktiviertel offenen Moros",
        "Ich möchte das zu den offenen Motus startes",
        "Startet den offenen Modus",
        "Würdest du den offenen Modus starten"
    ],
    "start_application": [
        "Beginn mit der Anwendung",
        "Start",
        "Starten",
        "Startet die Anwendung",
        "Startet die Applikation"
    ],
    "stop_application": [
        "Beende die Applikation",
        "Beendet die Anbindung",
        "Schließe die Applikation",
        "Stop",
        "Stoppe die Anwendung"
    ],
    "tell_next_step": [
        "Was ist der nächste Schritt",
        "Was muss ich als nächstes machen",
        "Was muss ich tun",
        "Wie funktioniert der nächste Schritt",
        "Wie geht es vor"
    ]
}
# Testfunktion
def test_intent_predictor(test_sentences):
    


    
    for intent, sentences in test_sentences.items():
        for sentence in sentences:
            predicted_label, probability = predictor.predict(sentence.lower())
            match_result = "Übereinstimmung" if predicted_label == intent else "Keine Übereinstimmung"
            print(f"Text: {sentence}\nErwarteter Intent: {intent}\nVorhergesagtes Label: {predicted_label} mit Wahrscheinlichkeit: {probability:.4f} - {match_result}\n")

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import precision_score, recall_score, f1_score, confusion_matrix
import pandas as pd

def extended_analysis(test_sentences, predictor):
    true_labels = []
    predicted_labels = []
    probabilities = []
    sentence_lengths = []
    false_positive_sentences = []
    false_negative_sentences = []
    true_positive_count = 0
    true_negative_count = 0
    false_positive_count = 0
    false_negative_count = 0
    intent_stats = {}

    for intent, sentences in test_sentences.items():
        correct_count = 0
        total_count = len(sentences)
        intent_probs = []
        intent_lengths = []

        for sentence in sentences:
            true_labels.append(intent)
            label, prob = predictor.predict(sentence.lower())  # Klassifizierung
            predicted_labels.append(label)
            probabilities.append(prob)
            sentence_length = len(sentence.split())
            sentence_lengths.append(sentence_length)
            intent_probs.append(prob)
            intent_lengths.append(sentence_length)
            
            # False Positives zählen (Falscher Intent, aber hohe Wahrscheinlichkeit)
            if label != intent and prob > 0.7:
                false_positive_count += 1
                false_positive_sentences.append((sentence, label, prob, intent))
            
            # False Negatives zählen (richtiger Intent wurde nicht erkannt)
            if label != intent and prob < 0.7:
                false_negative_count += 1
                false_negative_sentences.append((sentence, label, prob, intent))
            
            # True Positives zählen
            if label == intent and prob >= 0.7:
                true_positive_count += 1
            
            # True Negatives zählen
            if label == 'no_intent' and intent != 'no_intent' and prob < 0.7:
                true_negative_count += 1

        avg_prob = np.mean(intent_probs)
        max_prob = np.max(intent_probs)
        min_prob = np.min(intent_probs)
        std_prob = np.std(intent_probs)
        avg_sentence_length = np.mean(intent_lengths)

        intent_stats[intent] = {
            "Sätze": total_count,
            "Durchschnittliche Wahrscheinlichkeit (%)": avg_prob * 100,
            "Maximale Wahrscheinlichkeit (%)": max_prob * 100,
            "Minimale Wahrscheinlichkeit (%)": min_prob * 100,
            "Standardabweichung der Wahrscheinlichkeiten": std_prob * 100,
            "Anzahl der False Positives": false_positive_count,
            "Durchschnittliche Satzlänge (Wörter)": avg_sentence_length
        }

    # Gesamtstatistik berechnen
    total_probs = np.array(probabilities)
    avg_total_prob = np.mean(total_probs) * 100
    max_total_prob = np.max(total_probs) * 100
    min_total_prob = np.min(total_probs) * 100
    std_total_prob = np.std(total_probs) * 100
    avg_sentence_length_total = np.mean(sentence_lengths)

    intent_stats["Gesamtstatistik"] = {
        "Sätze": len(true_labels),
        "Durchschnittliche Wahrscheinlichkeit (%)": avg_total_prob,
        "Maximale Wahrscheinlichkeit (%)": max_total_prob,
        "Minimale Wahrscheinlichkeit (%)": min_total_prob,
        "Standardabweichung der Wahrscheinlichkeiten": std_total_prob,
        "Anzahl der False Positives": len(false_positive_sentences),
        "Durchschnittliche Satzlänge (Wörter)": avg_sentence_length_total
    }

    df_stats = pd.DataFrame(intent_stats).T
    df_stats = df_stats.sort_values("Durchschnittliche Wahrscheinlichkeit (%)", ascending=False)

    df_stats.to_csv("detailed_intent_statistic.csv", index=True)
    print("📊 Die detaillierten Statistiken wurden in 'detailed_intent_statistic.csv' gespeichert.")

    labels = [
        "arbeitsmodus", "check_count_große_schraube", "check_count_kleine_schraube",
        "check_count_oberteil", "check_count_spitze", "check_griff", "check_große_schraube",
        "check_kleine_schraube", "check_spitze", "drop_all", "drop_griff", "drop_große_schraube",
        "drop_kleine_schraube", "drop_spitze", "give_griff", "give_große_schraube", "give_kleine_schraube",
        "give_tip_or_bottom", "open_linken_greifer", "open_rechten_greifer", "do_next_step",
        "offener_modus", "start_application", "stop_application", "tell_next_step",
    ]

    # Metrics
    accuracy = np.mean(np.array(predicted_labels) == np.array(true_labels))
    precision = precision_score(true_labels, predicted_labels, average='weighted', zero_division=1)
    recall = recall_score(true_labels, predicted_labels, average='weighted', zero_division=1)
    f1 = f1_score(true_labels, predicted_labels, average='weighted', zero_division=1)
    misclassification_rate = np.mean(np.array(predicted_labels) != np.array(true_labels))
    cm = confusion_matrix(true_labels, predicted_labels, labels=labels)
    total_sentences = len(true_labels)

    # Metrics für die zusätzliche Confusion Matrix
    tn = true_negative_count
    fp = false_positive_count
    fn = false_negative_count
    tp = true_positive_count

    # Confusion Matrix für TN, FP, FN, TP
    cm_extended = np.array([[tp, fp],
                            [fn, tn]])

    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # Confusion Matrix der normalen Vorhersagen
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=False, ax=axes[0, 0], xticklabels=labels, yticklabels=labels)
    axes[0, 0].set_title("Confusion Matrix (Normale Vorhersagen)")
    axes[0, 0].set_xlabel("Vorhergesagte Labels")
    axes[0, 0].set_ylabel("Wahre Labels")

    # Distribution der Vorhersagewahrscheinlichkeiten
    axes[0, 1].hist(probabilities, bins=50, alpha=0.75, color='blue', edgecolor='black')
    axes[0, 1].set_title("Verteilung der Vorhersagewahrscheinlichkeiten")
    axes[0, 1].set_xlabel("Wahrscheinlichkeit")
    axes[0, 1].set_ylabel("Anzahl der Sätze")

    # Metriken
    axes[1, 0].bar(["Precision", "Recall", "F1-Score"], [precision, recall, f1], color='green')
    axes[1, 0].set_title("Metriken")
    axes[1, 0].set_ylabel("Wert")

    # Metriken und False Positives
    axes[1, 0].bar(["Precision", "Recall", "F1-Score", "False Positives (%)"],
                   [precision, recall, f1, (false_positive_count / total_sentences)],
                   color=['green', 'blue', 'orange', 'red'])

    axes[1, 0].set_title("Metriken & False Positives")
    axes[1, 0].set_ylabel("Wert")

    # Distribution der Satzlängen
    axes[1, 1].hist(sentence_lengths, bins=50, alpha=0.75, color='orange', edgecolor='black')
    axes[1, 1].set_title("Verteilung der Satzlängen")
    axes[1, 1].set_xlabel("Satzlänge (Wörter)")
    axes[1, 1].set_ylabel("Anzahl der Sätze")

    # Erweiterte Confusion Matrix an Position (1,1)
    sns.heatmap(cm_extended, annot=True, fmt='d', cmap='Reds', cbar=False, ax=axes[1, 1])
    axes[1, 1].set_title("Confusion Matrix (TN, FP, FN, TP)")
    axes[1, 1].set_xlabel("Predicted")
    axes[1, 1].set_ylabel("True")

    plt.tight_layout()
    plt.savefig("intent_analysis.png")
    plt.show()

    return intent_stats


intent_pr = IntentPredictor()
extended_analysis(test_sentences,intent_pr)