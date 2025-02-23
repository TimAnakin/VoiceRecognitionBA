import cv2
from ultralytics import YOLO
from ultralytics.utils.plotting import Annotator 


model = YOLO(r"C:\Users\timan\OneDrive\Desktop\robot_voice_control-1\voice_recognition_testing\UNILOKK_detection.pt");


cap = cv2.VideoCapture(2)
cap.set(3, 640)
cap.set(4, 480)



def detect_bounding_boxes():
    while True:
        _, img = cap.read()
        results = model.predict(img)
        
        annotator = Annotator(img)
        
        for r in results:
            boxes = r.boxes
            for box in boxes:
                b = box.xyxy[0]  # Bounding Box-Koordinaten
                c = box.cls
                annotator.box_label(b, model.names[int(c)])
        
        img = annotator.result()
        cv2.imshow('YOLO V8 Detection - Second Model', img)
        
        if cv2.waitKey(1) & 0xFF == ord(' '):
            break
    
# Starte die Erkennung

detect_bounding_boxes()

# Kamera freigeben und Fenster schließen
cap.release()
cv2.destroyAllWindows()
