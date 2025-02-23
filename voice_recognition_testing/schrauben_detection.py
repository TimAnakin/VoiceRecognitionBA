import cv2
from ultralytics import YOLO
from ultralytics.utils.plotting import Annotator
from Robot_Communication import robot_communication;

# Modell laden
model = YOLO(r"C:\Users\timan\OneDrive\Desktop\robot_voice_control-1\voice_recognition_testing\schrauben_model.pt")

# Kamera initialisieren
cap = cv2.VideoCapture(1)
cap.set(3, 640)
cap.set(4, 480)

# Definiere die relevanten Klassen
kleine_schrauben_labels = ["empty_kl_schraube", "kl_schraube"]
große_schrauben_labels = ["empty_gr_schraube", "gr_schraube"]

# Mapping für 0 und 1
class_to_binary = {
    "empty_kl_schraube": 0,
    "kl_schraube": 1,
    "empty_gr_schraube": 0,
    "gr_schraube": 1
}

def swap_pairs(lst):
    """Tauscht benachbarte Elemente der Liste paarweise."""
    for i in range(0, len(lst) - 1, 2):
        lst[i], lst[i + 1] = lst[i + 1], lst[i]
    return lst

def detect_and_sort_schrauben():
    while True:
        _, img = cap.read()
        results = model.predict(img)
        annotator = Annotator(img)

        # Listen für Bounding Boxes
        kleine_schrauben = []
        große_schrauben = []

        for r in results:
            boxes = r.boxes
            for box in boxes:
                b = box.xyxy[0].tolist()  # Bounding Box-Koordinaten als Liste
                c = int(box.cls)  # Klassennummer
                label = model.names[c]  # Klassenname

                # Bounding Box-Daten speichern
                bbox_data = {
                    "class": label,
                    "coordinates": {
                        "left": int(b[0]),
                        "top": int(b[1]),
                        "right": int(b[2]),
                        "bottom": int(b[3])
                    },
                    "center_x": (b[0] + b[2]) / 2,
                    "center_y": (b[1] + b[3]) / 2
                }

                # Bounding Box der passenden Liste hinzufügen
                if label in kleine_schrauben_labels:
                    kleine_schrauben.append(bbox_data)
                elif label in große_schrauben_labels:
                    große_schrauben.append(bbox_data)

                # Bounding Box im Bild markieren
                annotator.box_label(b, label)

        img = annotator.result()
        cv2.imshow('YOLO V8 Detection', img)

        # 🛠 Sortierung der Bounding Boxes nach räumlicher Position
        kleine_schrauben.sort(key=lambda b: (b["center_y"], b["center_x"]))
        große_schrauben.sort(key=lambda b: (b["center_y"], b["center_x"]))

        # 🛠 Tausche paarweise die Reihenfolge der Schrauben
        if len(kleine_schrauben) == 8:
            kleine_schrauben = swap_pairs(kleine_schrauben)

        if len(große_schrauben) == 8:
            große_schrauben = swap_pairs(große_schrauben)

        # Konvertiere die Listen in Arrays mit 0 und 1
        kleine_schrauben_bin = [class_to_binary[b["class"]] for b in kleine_schrauben]
        große_schrauben_bin = [class_to_binary[b["class"]] for b in große_schrauben]

     
        print(kleine_schrauben_bin)

        print(große_schrauben_bin)

        # Prüfen, ob jeweils genau 8 Elemente in beiden Listen sind
        if len(kleine_schrauben) == 8 and len(große_schrauben) == 8:
            print("\n✅ Alle 8 kleinen und 8 großen Schrauben wurden erkannt. Beende die Schleife.")
            return kleine_schrauben_bin,große_schrauben_bin

        else:
            print("\n⚠️ Noch nicht alle Schrauben erkannt! Suche weiter...")

        # Beenden, wenn Leertaste gedrückt wird
        if cv2.waitKey(1) & 0xFF == ord(' '):
            print("\n⏹ Manuelles Beenden erkannt. Stoppe die Erkennung.")
            break



def get_kl_schraube_into_halterung():           
    kl_schraube_box,gr_schraube_box =detect_and_sort_schrauben()
    num = 1;
    print(kl_schraube_box)
    for value in kl_schraube_box:
                
                if value == 1:
                    value = 0;
                    robot_communication.kleineSchraube_sorted(num)
                    robot_communication.drop_kl_schraube();
                    return;
                else:
                    num += 1;
                    if num > 8:
                         print("Griffe nachfüllen, sind alle")

def get_gr_schraube_into_halterung():           
    kl_schraube_box,gr_schraube_box =detect_and_sort_schrauben()
    iterator = 1;
    for value in gr_schraube_box:
                if value == 1:
                    value = 0;
                    robot_communication.großeSchraube_sorted(iterator)
                    robot_communication.drop_gr_schraube();
                    break;
                else:
                    num += 1;
                    if num > 8:
                         print("Griffe nachfüllen, sind alle")
def give_kl_schraube():           
    kl_schraube_box,gr_schraube_box =detect_and_sort_schrauben()
    iterator = 1;
    for value in kl_schraube_box:
                if value == 1:
                    value = 0;
                    robot_communication.großeSchraube_sorted(iterator)
                    robot_communication.give_kl_schraube();
                    break;
                else:
                    num += 1;
                    if num > 8:
                         print("kleine Schrauben nachfüllen, sind alle")
def give_gr_schraube():           
    kl_schraube_box,gr_schraube_box =detect_and_sort_schrauben()
    iterator = 1;
    for value in gr_schraube_box:
                if value == 1:
                    value = 0;
                    robot_communication.großeSchraube_sorted(iterator)
                    robot_communication.give_gr_schraube();
                    break;
                else:
                    num += 1;
                    if num > 8:
                         print("Große Schrauben nachfüllen, sind alle")
def check_count_kl_schraube():
    kl_schraube_box,gr_schraube_box =detect_and_sort_schrauben()
    num = 0;
    for value in kl_schraube_box:
                if value == 1:
                    num += 1
    return num;

def check_count_gr_schraube():
    kl_schraube_box,gr_schraube_box =detect_and_sort_schrauben()
    num = 0;
    for value in gr_schraube_box:
                if value == 1:
                    num += 1
    return num;
def check_kl_schraube():
    kl_schraube_box,gr_schraube_box =detect_and_sort_schrauben()
    
    for value in kl_schraube_box:
                if value == 1:
                    return True
def check_gr_schraube():
    kl_schraube_box,gr_schraube_box =detect_and_sort_schrauben()
    
    for value in gr_schraube_box:
                if value == 1:
                    return True


if __name__ == "__main__":

    cap.release()
    cv2.destroyAllWindows()


