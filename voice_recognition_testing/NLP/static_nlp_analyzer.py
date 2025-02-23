import spacy

# Lade spaCy-Modell (hier für Deutsch)
nlp = spacy.load("de_core_news_lg")

intents = {
  "check_griff": [
    "Sind noch Oberteile vorhanden?",
    "Hast du noch Oberteile?",
    "Gibt es noch Oberteile?",
    "Sind Oberteile noch verfügbar?",
    "Sind noch Oberteile im Lager?",
    "Existieren noch Oberteile?",
    "Sind Oberteile noch auf Lager?",
    "Überprüfe, ob noch Oberteile vorhanden sind",
    "Kannst du prüfen, ob Oberteile verfügbar sind?",
    "Prüfe, ob noch Oberteile im Bestand sind",
    "Checke nach Oberteilen",
    "Ist das Oberteil noch vorhanden?",
    "Existieren noch Oberteile im Lager?",
    "Gibt es Restbestände von Oberteilen?",
    "Sind noch Oberteile übrig?",
    "Sind Oberteile vorrätig?",
    "Hast du noch Oberteile im Lager?",
    "Prüfe, ob es noch Oberteile gibt",
    "Checke nach Oberteilen im Bestand",
    "Überprüfe, ob noch Oberteile auf Lager sind",
    "Sind noch Griffe vorhanden?",
    "Hast du noch Griffe?",
    "Gibt es noch Griffe?",
    "Sind Griffe noch verfügbar?",
    "Sind noch Griffe im Lager?",
    "Existieren noch Griffe?",
    "Sind Griffe noch auf Lager?",
    "Überprüfe, ob noch Griffe vorhanden sind",
    "Kannst du prüfen, ob Griffe verfügbar sind?",
    "Prüfe, ob noch Griffe im Bestand sind",
    "Checke nach Griffen",
    "Ist der Griff noch vorhanden?",
    "Existieren noch Griffe im Lager?",
    "Gibt es Restbestände von Griffen?",
    "Sind noch Griffe übrig?",
    "Sind Griffe vorrätig?",
    "Hast du noch Griffe im Lager?",
    "Prüfe, ob es noch Griffe gibt",
    "Checke nach Griffen im Bestand",
    "Überprüfe, ob noch Griffe auf Lager sind"
  ],
  "check_spitze": [
    "Sind noch Unterteile vorhanden?",
    "Hast du noch Unterteile?",
    "Gibt es noch Unterteile?",
    "Hast du noch Spitzen?",
    "Sind Unterteile noch verfügbar?",
    "Sind noch Unterteile im Lager?",
    "Existieren noch Unterteile?",
    "Sind Unterteile noch auf Lager?",
    "Überprüfe, ob noch Unterteile vorhanden sind",
    "Kannst du prüfen, ob Unterteile verfügbar sind?",
    "Prüfe, ob noch Unterteile im Bestand sind",
    "Checke nach Unterteilen",
    "Ist das Unterteil noch vorhanden?",
    "Existieren noch Unterteile im Lager?",
    "Gibt es Restbestände von Unterteilen?",
    "Sind noch Unterteile übrig?",
    "Sind Unterteile vorrätig?",
    "Hast du noch Unterteile im Lager?",
    "Prüfe, ob es noch Unterteile gibt",
    "Checke nach Unterteilen im Bestand",
    "Überprüfe, ob noch Unterteile auf Lager sind",
    "Sind noch Spitzen vorhanden?",
    "Hast du noch Spitzen?",
    "Gibt es noch Spitzen?",
    "Sind Spitzen noch verfügbar?",
    "Sind noch Spitzen im Lager?",
    "Existieren noch Spitzen?",
    "Sind Spitzen noch auf Lager?",
    "Überprüfe, ob noch Spitzen vorhanden sind",
    "Kannst du prüfen, ob Spitzen verfügbar sind?",
    "Prüfe, ob noch Spitzen im Bestand sind",
    "Checke nach Spitzen",
    "Ist die Spitze noch vorhanden?",
    "Existieren noch Spitzen im Lager?",
    "Gibt es Restbestände von Spitzen?",
    "Sind noch Spitzen übrig?",
    "Sind Spitzen vorrätig?",
    "Hast du noch Spitzen im Lager?",
    "Prüfe, ob es noch Spitzen gibt",
    "Checke nach Spitzen im Bestand",
    "Überprüfe, ob noch Spitzen auf Lager sind"
  ],
   "next_step": [
    "Was ist der nächste Schritt",
    "Was muss ich als Nächstes tun",
    "Kannst du mir den nächsten Montageschritt sagen",
    "Was folgt jetzt",
    "Was passiert im nächsten Schritt",
    "Was soll ich jetzt machen",
    "Was ist der nächste Arbeitsschritt",
    "Was steht als Nächstes an",
    "Welcher Schritt kommt jetzt",
    "Wie geht es weiter",
    "Was kommt nach diesem Schritt",
    "Kannst du den nächsten Schritt ansagen",
    "Bitte zeige mir den nächsten Schritt",
    "Wie lautet der nächste Befehl",
    "Was folgt nach dieser Aufgabe"
  ],

  "check_count_spitze": [
    "Wie viele Spitzen sind noch verfügbar?",
    "Wie viele Spitzen gibt es noch?",
    "Wie viele Spitzen hast du noch?",
    "Wie viele Spitzen sind im Lager?",
    "Wie viele Spitzen sind noch vorrätig?",
    "Wie viele Spitzen gibt es noch auf Lager?",
    "Wie viele Spitzen sind noch im Bestand?",
    "Wie viele Spitzen hast du im Lager?",
    "Wie viele Spitzen fehlen im Bestand?",
    "Wie viele Spitzen gibt es noch im Lager?",
    "Wie viele Spitzen sind noch auf Lager?",
    "Wie viele Spitzen sind noch übrig?",
    "Wie viele Spitzen hast du noch im Bestand?",
    "Wie viele Unterteile sind noch verfügbar?",
    "Wie viele Unterteile gibt es noch?",
    "Wie viele Unterteile hast du noch?",
    "Wie viele Unterteile sind im Lager?",
    "Wie viele Unterteile sind noch vorrätig?",
    "Wie viele Unterteile gibt es noch auf Lager?",
    "Wie viele Unterteile sind noch im Bestand?",
    "Wie viele Unterteile hast du im Lager?",
    "Wie viele Unterteile fehlen im Bestand?",
    "Wie viele Unterteile gibt es noch im Lager?",
    "Wie viele Unterteile sind noch auf Lager?",
    "Wie viele Unterteile sind noch übrig?",
    "Wie viele Unterteile hast du noch im Bestand?",
    "Sag mir die Anzahl an Spitzen",
    "Sag mir die Anzahl an Unterteilen",
    "Gib mir die Anzahl an noch vorhandenen Unterteilen",
    "Gib mir die Anzahl an noch vorhandenen Spitzen",
    "Checke die Anzahl an Spitzen",
    "Checke die Anzahl an Unterteilen"
  ],
  "check_count_oberteil_und_griff": [
    "Wie viele Oberteile sind noch verfügbar?",
    "Wie viele Oberteile gibt es noch?",
    "Wie viele Oberteile hast du noch?",
    "Wie viele Oberteile sind im Lager?",
    "Wie viele Oberteile sind noch vorrätig?",
    "Wie viele Oberteile gibt es noch auf Lager?",
    "Wie viele Oberteile sind noch im Bestand?",
    "Wie viele Oberteile hast du im Lager?",
    "Wie viele Oberteile fehlen im Bestand?",
    "Wie viele Oberteile gibt es noch im Lager?",
    "Wie viele Oberteile sind noch auf Lager?",
    "Wie viele Oberteile sind noch übrig?",
    "Wie viele Oberteile hast du noch im Bestand?",
    "Wie viele Griffe sind noch verfügbar?",
    "Wie viele Griffe gibt es noch?",
    "Wie viele Griffe hast du noch?",
    "Wie viele Griffe sind im Lager?",
    "Wie viele Griffe sind noch vorrätig?",
    "Wie viele Griffe gibt es noch auf Lager?",
    "Wie viele Griffe sind noch im Bestand?",
    "Wie viele Griffe hast du im Lager?",
    "Wie viele Griffe fehlen im Bestand?",
    "Wie viele Griffe gibt es noch im Lager?",
    "Wie viele Griffe sind noch auf Lager?",
    "Wie viele Griffe sind noch übrig?",
    "Wie viele Griffe hast du noch im Bestand?",
    "Sag mir die Anzahl an Oberteilen",
    "Sag mir die Anzahl an Griffen",
    "Gib mir die Anzahl an noch vorhandenen Oberteilen",
    "Gib mir die Anzahl an noch vorhandenen Griffen"
  ],
  "check_kleine_schraube": [
    "Sind noch kleine Schrauben vorhanden?",
    "Hast du noch kleine Schrauben?",
    "Gibt es noch kleine Schrauben?",
    "Sind kleine Schrauben noch verfügbar?",
    "Sind noch kleine Schrauben im Lager?",
    "Existieren noch kleine Schrauben?",
    "Sind kleine Schrauben noch auf Lager?",
    "Überprüfe, ob noch kleine Schrauben vorhanden sind",
    "Kannst du prüfen, ob kleine Schrauben verfügbar sind?",
    "Prüfe, ob noch kleine Schrauben im Bestand sind",
    "Checke nach kleinen Schrauben",
    "Ist die kleine Schraube noch vorhanden?",
    "Existieren noch kleine Schrauben im Lager?",
    "Gibt es Restbestände von kleinen Schrauben?",
    "Sind noch kleine Schrauben übrig?",
    "Sind kleine Schrauben vorrätig?",
    "Hast du noch kleine Schrauben im Lager?",
    "Prüfe, ob es noch kleine Schrauben gibt",
    "Checke nach kleinen Schrauben im Bestand",
    "Überprüfe, ob noch kleine Schrauben auf Lager sind"
  ],
  "check_grosse_schraube": [
    "Sind noch große Schrauben vorhanden?",
    "Hast du noch große Schrauben?",
    "Gibt es noch große Schrauben?",
    "Sind große Schrauben noch verfügbar?",
    "Sind noch große Schrauben im Lager?",
    "Existieren noch große Schrauben?",
    "Sind große Schrauben noch auf Lager?",
    "Überprüfe, ob noch große Schrauben vorhanden sind",
    "Kannst du prüfen, ob große Schrauben verfügbar sind?",
    "Prüfe, ob noch große Schrauben im Bestand sind",
    "Checke nach großen Schrauben",
    "Ist die große Schraube noch vorhanden?",
    "Existieren noch große Schrauben im Lager?",
    "Gibt es Restbestände von großen Schrauben?",
    "Sind noch große Schrauben übrig?",
    "Sind große Schrauben vorrätig?",
    "Hast du noch große Schrauben im Lager?",
    "Prüfe, ob es noch große Schrauben gibt",
    "Checke nach großen Schrauben im Bestand",
    "Überprüfe, ob noch große Schrauben auf Lager sind"
  ],
  "lass_fallen_links": [
    "Öffne den linken Greifer",
    "Mach den linken Greifer auf",
    "Lass den linken Greifer los",
    "Löse den linken Greifer",
    "Linker Greifer öffnen",
    "Mach den linken Greifer locker",
    "Lass links los",
    "Greifer links öffnen",
    "Bitte öffne den linken Greifer",
    "Sei so gut und öffne den linken Greifer",
    "Lass den linken Greifer einfach los",
    "Mach den linken Greifer auf",
    "Kannst du den linken Greifer aufmachen",
    "Könntest du den linken Greifer lösen",
    "Bitte lass den linken Greifer los",
    "Lass die linke Seite los",
    "Beende den linken Griff",
    "Mach links auf",
    "Linke Seite öffnen",
    "Löse die linke Seite"
  ],
  "lass_fallen_rechts": [
    "Öffne den rechten Greifer",
    "Mach den rechten Greifer auf",
    "Lass den rechten Greifer los",
    "Löse den rechten Greifer",
    "Rechter Greifer öffnen",
    "Mach den rechten Greifer locker",
    "Lass rechts los",
    "Greifer rechts öffnen",
    "Bitte öffne den rechten Greifer",
    "Sei so gut und öffne den rechten Greifer",
    "Lass den rechten Greifer einfach los",
    "Mach den rechten Greifer auf",
    "Kannst du den rechten Greifer aufmachen",
    "Könntest du den rechten Greifer lösen",
    "Bitte lass den rechten Greifer los",
    "Lass die rechte Seite los",
    "Beende den rechten Griff",
    "Mach rechts auf",
    "Rechte Seite öffnen",
    "Löse die rechte Seite"
  ],
   "check_count_kleine_schraube": [
    "Wie viele kleine Schrauben sind noch verfügbar?",
    "Wie viele kleine Schrauben gibt es noch?",
    "Wie viele kleine Schrauben hast du noch?",
    "Wie viele kleine Schrauben sind im Lager?",
    "Wie viele kleine Schrauben sind noch vorrätig?",
    "Wie viele kleine Schrauben gibt es noch auf Lager?",
    "Wie viele kleine Schrauben sind noch im Bestand?",
    "Wie viele kleine Schrauben hast du im Lager?",
    "Wie viele kleine Schrauben fehlen im Bestand?",
    "Wie viele kleine Schrauben gibt es noch im Lager?",
    "Wie viele kleine Schrauben sind noch auf Lager?",
    "Wie viele kleine Schrauben sind noch übrig?",
    "Wie viele kleine Schrauben hast du noch im Bestand?",
    "Sag mir die Anzahl an kleinen Schrauben",
    "Gib mir die Anzahl an noch vorhandenen kleinen Schrauben",
    "Checke die Anzahl an kleinen Schrauben",
    "Zähle die verbleibenden kleinen Schrauben",
    "Wie viele kleine Schrauben sind noch da?",
    "Wie viele kleine Schrauben gibt es im Lager?"
  ],
  "check_count_grosse_schraube": [
    "Wie viele große Schrauben sind noch verfügbar?",
    "Wie viele große Schrauben gibt es noch?",
    "Wie viele große Schrauben hast du noch?",
    "Wie viele große Schrauben sind im Lager?",
    "Wie viele große Schrauben sind noch vorrätig?",
    "Wie viele große Schrauben gibt es noch auf Lager?",
    "Wie viele große Schrauben sind noch im Bestand?",
    "Wie viele große Schrauben hast du im Lager?",
    "Wie viele große Schrauben fehlen im Bestand?",
    "Wie viele große Schrauben gibt es noch im Lager?",
    "Wie viele große Schrauben sind noch auf Lager?",
    "Wie viele große Schrauben sind noch übrig?",
    "Wie viele große Schrauben hast du noch im Bestand?",
    "Sag mir die Anzahl an großen Schrauben",
    "Gib mir die Anzahl an noch vorhandenen großen Schrauben",
    "Checke die Anzahl an großen Schrauben",
    "Zähle die verbleibenden großen Schrauben",
    "Wie viele große Schrauben sind noch da?",
    "Wie viele große Schrauben gibt es im Lager?"
  ],
   "give_small_screw": [
      "Gib mir die kleine Schraube",
      "Kannst du mir bitte die kleine Schraube geben",
      "Reich mir die kleine Schraube",
      "Ich brauche die kleine Schraube",
      "Hol mir die kleine Schraube",
      "Bring mir die kleine Schraube",
      "Könntest du mir die kleine Schraube reichen",
      "Reich mir bitte die kleine Schraube",
      "Hast du die kleine Schraube für mich",
      "Hol bitte die kleine Schraube für mich"
    ],
    "give_large_screw": [
      "Gib mir die große Schraube",
      "Kannst du mir bitte die große Schraube geben",
      "Reich mir die große Schraube",
      "Ich brauche die große Schraube",
      "Hol mir die große Schraube",
      "Bring mir die große Schraube",
      "Könntest du mir die große Schraube reichen",
      "Reich mir bitte die große Schraube",
      "Hast du die große Schraube für mich",
      "Hol bitte die große Schraube für mich"
    ],
    "give_grip_or_top": [
      "Gib mir den Griff",
      "Kannst du mir bitte den Griff geben",
      "Reich mir den Griff",
      "Ich brauche den Griff",
      "Hol mir den Griff",
      "Bring mir den Griff",
      "Könntest du mir den Griff reichen",
      "Reich mir bitte den Griff",
      "Hast du den Griff für mich",
      "Hol bitte den Griff für mich",
      "Gib mir das Oberteil",
      "Kannst du mir bitte das Oberteil geben",
      "Reich mir das Oberteil",
      "Ich brauche das Oberteil",
      "Hol mir das Oberteil",
      "Bring mir das Oberteil",
      "Könntest du mir das Oberteil reichen",
      "Reich mir bitte das Oberteil",
      "Hast du das Oberteil für mich",
      "Hol bitte das Oberteil für mich"
    ],
    "give_tip_or_bottom": [
      "Gib mir die Spitze",
      "Kannst du mir bitte die Spitze geben",
      "Reich mir die Spitze",
      "Ich brauche die Spitze",
      "Hol mir die Spitze",
      "Bring mir die Spitze",
      "Könntest du mir die Spitze reichen",
      "Reich mir bitte die Spitze",
      "Hast du die Spitze für mich",
      "Hol bitte die Spitze für mich",
      "Gib mir das Unterteil",
      "Kannst du mir bitte das Unterteil geben",
      "Reich mir das Unterteil",
      "Ich brauche das Unterteil",
      "Hol mir das Unterteil",
      "Bring mir das Unterteil",
      "Könntest du mir das Unterteil reichen",
      "Reich mir bitte das Unterteil",
      "Hast du das Unterteil für mich",
      "Hol bitte das Unterteil für mich"
    ]

}

# Funktion zum Vorverarbeiten von Text
def preprocess_text(text):
    doc = nlp(text.lower())
    # Erstelle eine Liste mit Lemma, Head-Lemma und Abhängigkeits-Tag
    processed = [(token.lemma_, token.head.lemma_, token.dep_) for token in doc]
    return processed

# Funktion zur Erkennung des Befehls
def check_command(user_input):
    processed_input = preprocess_text(user_input)
    print(f"Verarbeiteter Eingabetext: {processed_input}")
    
    # Phase 1: Prüfen auf exakte Übereinstimmung (alle 3 Werte)
    for command, keywords in commands.items():
        for keyword in keywords:
            processed_keyword = preprocess_text(keyword)
            print(f"Verarbeitetes Keyword für {command}: {processed_keyword}")
            
            for processed_token in processed_input:
                for keyword_token in processed_keyword:
                    if processed_token == keyword_token:  # Exakte Übereinstimmung
                        print(f"Exakter Befehl erkannt: {command}")
                        return command
    
    # Phase 2: Fallback - Prüfen auf Übereinstimmung nur mit dem Lemma
    for command, keywords in commands.items():
        for keyword in keywords:
            processed_keyword = preprocess_text(keyword)
            for processed_token in processed_input:
                for keyword_token in processed_keyword:
                    if processed_token[0] == keyword_token[0]:  # Nur das Lemma vergleichen
                        print(f"Fallback-Befehl erkannt: {command}")
                        return command

    return "Unbekannter Befehl"

def detect_intent_with_vectors(user_input):
    user_doc = nlp(user_input.lower())
    best_intent = "Unknown"
    max_similarity = 0

    for intent, examples in intents.items():
        for example in examples:
            example_doc = nlp(example.lower())
            similarity = user_doc.similarity(example_doc)
            if similarity > max_similarity:
                max_similarity = similarity
                best_intent = intent

    return best_intent if max_similarity > 0.9 else "Unknown", max_similarity  # Setze Threshold bei 0.7

# Teste die Funktion mit neuen Satzvariationen
user_inputs = [
    "Sind noch Unterteile verfügbar",
    "Hast du Griffe",
    "Wie viele große Schrauben gibt es noch?",
    "Sind kleine Teile vorhanden",
    "Hast du noch Mini-Schrauben",
    "Gibt es Schrauben groß",
    "Ist die Spitze noch verfügbar",
    "Ich würde gerne wissen, wie viele Spitzen noch da sind",
    "lege eine kleine Schraube in die Zone xy",
    "Ich brauche Schrauben für ein Oberteil. Sind noch welche da“"
]

# Teste die Synonym Funktion
for user_input in user_inputs:
    intent, similarity = detect_intent_with_vectors(user_input)
    print(f"Benutzeranfrage: '{user_input}'")
    # print(f"Erkannter Intent: {intent} (Ähnlichkeit: {similarity:.2f})")
    # print("-" * 50)
user_input = "Hast du noch große Schrauben"
command = check_command(user_input)
print(f"Erkannter Befehl: {command}")
