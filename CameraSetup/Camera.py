import cv2
import numpy as np

# Kamera starten
cap = cv2.VideoCapture(1)

if not cap.isOpened():
    print("Fehler: Kamera konnte nicht geöffnet werden.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Fehler: Kein Bild von der Kamera erhalten.")
        break

    # Bildvorverarbeitung
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)    
    edges = cv2.Canny(blurred, 50, 150)            

    
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in contours:
        # Bounding Box erstellen
        x, y, w, h = cv2.boundingRect(contour)
        
        if w > 20 and h > 20:  
            
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
          
            cv2.putText(frame, f"W:{w}, H:{h}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

    cv2.imshow('Objekterkennung', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
