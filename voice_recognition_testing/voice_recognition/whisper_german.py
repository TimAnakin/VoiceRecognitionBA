import speech_recognition as sr
from transformers import AutoProcessor, AutoModelForSpeechSeq2Seq, pipeline
import torch

# Whisper-Modell laden
device = "cuda" if torch.cuda.is_available() else "cpu"
model_id = "openai/whisper-large"
model = AutoModelForSpeechSeq2Seq.from_pretrained(model_id).to(device)
processor = AutoProcessor.from_pretrained(model_id)

# Spracherkennungs-Pipeline erstellen
pipe = pipeline(
    "automatic-speech-recognition",
    model=model,
    tokenizer=processor.tokenizer,
    feature_extractor=processor.feature_extractor,
    device=device,
)

# Sprachbefehl erkennen und mit Whisper transkribieren
def speech_to_text_whisper():
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Warte auf Sprachbefehl...")
        recognizer.adjust_for_ambient_noise(source, duration=1)  # Umgebungsgeräusche anpassen
        
        try:
            audio = recognizer.listen(source, timeout=10, phrase_time_limit=5)
            print("Verarbeite...")

            # Audio in Datei speichern, damit Whisper es verwenden kann
            with open("audio.wav", "wb") as f:
                f.write(audio.get_wav_data())

            # Whisper verwenden, um Sprache zu Text zu konvertieren
            result = pipe("audio.wav")
            print(f"Erkannter Befehl: {result['text']}")
            return result['text']

        except sr.UnknownValueError:
            print("Konnte den Befehl nicht verstehen.")
            return None
        except sr.RequestError as e:
            print(f"Fehler beim Abrufen der Ergebnisse: {e}")
            return None

# Funktion aufrufen
speech_to_text_whisper()
