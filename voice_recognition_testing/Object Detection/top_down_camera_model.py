from ultralytics import YOLO

# YOLOv8-Modell initialisieren
model = YOLO("yolov8n.pt")  # Verwende "yolov8n.pt" (Nano) oder andere Varianten

# Training starten
model.train(
    data="C:/Users/Tim/Downloads/checking/config.yaml",      # Pfad zur YAML-Datei
    epochs=80, 
                  
)
