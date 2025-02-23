from RealtimeSTT import AudioToTextRecorder
import pyautogui
import keyboard

# Variable, um den erkannten Text zu speichern
recognized_text = ""

def process_text(text):
    global recognized_text  # Zugriff auf die globale Variable
    recognized_text = text  # Speichere den erkannten Text
    print("Erkannter Text:", recognized_text)

if __name__ == '__main__':
    print("Wait until it says 'speak now'")
    recorder = AudioToTextRecorder(language="de", input_device_index=3)

    while True:
        recorder.text(process_text)  # Der Text wird in process_text gespeichert

        # Falls du den Text außerhalb der Funktion nutzen möchtest:
        if recognized_text:
            print(f"Gespeicherter Text: {recognized_text}")

            