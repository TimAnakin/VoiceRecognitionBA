import cv2
from ultralytics import YOLO
from ultralytics.utils.plotting import Annotator 
from itertools import zip_longest
import schrauben_detection;
from Robot_Communication import robot_communication
# Trainiertes Modell laden
#model = YOLO(r"C:\Users\Tim\Desktop\VoiceRecognitionTimSuelz\voice_recognition_testing\best.pt")
model = YOLO(r"C:\Users\timan\OneDrive\Desktop\robot_voice_control-1\voice_recognition_testing\model_for_top_cam.pt");

def calculate_mean(values):
    if len(values) == 0:
        return 0 
    return sum(values) / len(values)

def combine_alternating(left_zone_sort, right_zone_sort):
    combined_zones_sorted = [
        item 
        for pair in zip_longest(left_zone_sort, right_zone_sort) 
        for item in pair if item is not None
    ]
    return combined_zones_sorted

    
def sort_bbox(halterung_objects):
    for bbox in halterung_objects:
        bbox['center_y'] = (bbox['coordinates']['top'] + bbox['coordinates']['bottom']) / 2
        bbox['center_x'] = (bbox['coordinates']['left'] + bbox['coordinates']['right']) / 2
    center_x_values = [bbox['center_x'] for bbox in halterung_objects]
    threshold = calculate_mean(center_x_values)

    
    left_zone = []
    right_zone = []
    
    # Clustern der Bounding Boxes basierend auf dem Schwellenwert
    for bbox in halterung_objects:
        if bbox['center_x'] <= threshold:
            
            left_zone.append(bbox)
        else:
            
            right_zone.append(bbox)

    left_zone_sorted = sorted(left_zone, key=lambda bbox: bbox['center_y'], reverse=True)
    right_zone_sorted = sorted(right_zone, key=lambda bbox: bbox['center_y'],reverse=True)
    

    
    combined_list =  combine_alternating(right_zone_sorted,left_zone_sorted)
    
    return combined_list

    
    
cap = cv2.VideoCapture(3)
cap.set(3, 640)
cap.set(4, 480)
ROI_TOP = 187
ROI_BOTTOM = 280
ROI_LEFT = 220
ROI_RIGHT = 360
 

def find_position_empty_not_empty():
        while True:
            _, img = cap.read()
            
            # BGR to RGB conversion is performed under the hood
            # see: https://github.com/ultralytics/ultralytics/issues/2575
            results = model.predict(img)
            bounding_boxes = []
            halterung_griff_boxes = []
            halterung_spitze_boxes = []
            empty_boxes = []
            not_empty_boxes = []
            in_halterung_spitze = []
            halterung_g_bbox = []
            halterung_s_bbox =[]
            in_halterung_griff = []
            for r in results:
                
                annotator = Annotator(img)
                
                boxes = r.boxes
                for box in boxes:
                    
                    b = box.xyxy[0]  # get box coordinates in (left, top, right, bottom) format
                    c = box.cls
                    annotator.box_label(b, model.names[int(c)])

                    bounding_boxes.append({
                        "class": model.names[int(c)],
                        "coordinates": {
                            "left": int(b[0]) + ROI_LEFT,
                            "top": int(b[1]) + ROI_TOP,
                            "right": int(b[2])+ ROI_RIGHT,
                            "bottom": int(b[3] + ROI_BOTTOM)
                        },
                        "confidence": box.conf
                    })
                
            img = annotator.result()  
            cv2.imshow('YOLO V8 Detection', img)     
            if cv2.waitKey(1) & 0xFF == ord(' '):
                break
            for bbox in bounding_boxes:
                if bbox['class'] == "Halterung_griff":
                        print(2)
                        halterung_griff_boxes.append(bbox)
                elif bbox['class'] == "Halterung_spitze":
                        print(3)
                        halterung_spitze_boxes.append(bbox)
                elif bbox['class'] == "empty":
                        empty_boxes.append(bbox)
                elif bbox['class'] == "not_empty":
                        not_empty_boxes.append(bbox)

            for empty_bbox in empty_boxes:
                center_x = (empty_bbox['coordinates']['left'] + empty_bbox['coordinates']['right']) / 2
                center_y = (empty_bbox['coordinates']['top'] + empty_bbox['coordinates']['bottom']) / 2
                for griff_box in halterung_griff_boxes:
                    print(center_x)
                    print(center_y)
                    left = griff_box['coordinates']['left']
                    right = griff_box['coordinates']['right']
                    top = griff_box['coordinates']['top']
                    bottom = griff_box['coordinates']['bottom']
                    print(left, right,top,bottom)
                    if left <= center_x <= right and top <= center_y <= bottom:
                        in_halterung_griff.append(empty_bbox)
                    else:
                        in_halterung_spitze.append(empty_bbox)

            for not_empty_bbox in not_empty_boxes:
                center_x = (not_empty_bbox['coordinates']['left'] + not_empty_bbox['coordinates']['right']) / 2
                center_y = (not_empty_bbox['coordinates']['top'] + not_empty_bbox['coordinates']['bottom']) / 2
                for griff_box in halterung_griff_boxes:

                    left = griff_box['coordinates']['left']
                    right = griff_box['coordinates']['right']
                    top = griff_box['coordinates']['top']
                    bottom = griff_box['coordinates']['bottom']
                    if left <= center_x <= right and top <= center_y <= bottom:
                        in_halterung_griff.append(not_empty_bbox);
                    else:
                        in_halterung_spitze.append(not_empty_bbox)

            if len(in_halterung_griff) != 8:
                 print("nicht alle gefunden")
                 continue;
            if len(in_halterung_spitze)!=8:
                 print("Nicht alle gefunden")
                 continue;
                 
                
                
            print('Halterung Griff:')
            in_halterung_griff = sort_bbox(in_halterung_griff)

            print('Halterung Spitze:')
            in_halterung_spitze = sort_bbox(in_halterung_spitze)
            print("Halterung_Griff:")
            for box in in_halterung_griff:
                if box['class'] == "empty":
                    halterung_g_bbox.append(0)
                if box['class'] == "not_empty":
                     halterung_g_bbox.append(1)
                 
            print("Halterung_Spitze:")
            for box in in_halterung_spitze:
                if box['class'] == "empty":
                    halterung_s_bbox.append(0)
                if box['class'] == "not_empty":
                     halterung_s_bbox.append(1)
            
            print("Spitzbox:")
            print(halterung_s_bbox)
            print("Griffbox:")
            print(halterung_g_bbox)
            return halterung_g_bbox,halterung_s_bbox       

        
                 
                 
                      
                    
                           



    # er erkennt die richtigen seiten, der empty boxen. Reihenfolge stimmt auch, nur müssen noch sachen predicted werden, wenn etwas nicht klappt
def check_count_griff():
    g_box,s_box =find_position_empty_not_empty()
    num = 0;
    for value in g_box:
                if value == 1:
                    num += 1
    return num;

def check_count_spitze():
    g_box,s_box =find_position_empty_not_empty()
    num = 0;
    for value in s_box:
                if value == 1:
                    num += 1
    return num;
def check_griff():
    g_box,s_box =find_position_empty_not_empty()
    
    for value in g_box:
                if value == 1:
                    return True
def check_spitze():
    g_box,s_box =find_position_empty_not_empty()
    
    for value in s_box:
                if value == 1:
                    return True



def get_griff_into_halterung():           
    g_box,s_box =find_position_empty_not_empty()
    num = 1;
    for value in g_box:
                if value == 1:
                    value = 0;
                    robot_communication.griff_sorted(num)
                    robot_communication.drop_griff();
                    break;
                else:
                    num += 1;
                    if num > 8:
                         print("Griffe nachfüllen, sind alle")
def give_griff():           
    g_box,s_box =find_position_empty_not_empty()
    num = 1;
    for value in g_box:
                if value == 1:
                    value = 0;
                    robot_communication.griff_sorted(num)
                    robot_communication.give_griff();
                    break;
                else:
                    num += 1;
                    if num > 8:
                         print("Griffe nachfüllen, sind alle")
    

def get_spitze_into_halterung():
    g_box,s_box =find_position_empty_not_empty()
    num = 1;
    for value in s_box:
                if value == 1:
                    value = 0;
                    robot_communication.spitze_sorted(num)
                    robot_communication.drop_spitze();
                    break;
                else:
                    num += 1;
                    if num > 8:
                         print("Spitzen nachfüllen, sind alle")
def give_spitze():
    g_box,s_box =find_position_empty_not_empty()
    num = 1;
    for value in s_box:
                if value == 1:
                    value = 0;
                    robot_communication.spitze_sorted(num)
                    robot_communication.give_spitze();
                    break;
                else:
                    num += 1;
                    if num > 8:
                         print("Spitzen nachfüllen, sind alle")



def automodus():
        g_box,s_box =find_position_empty_not_empty()
        kl_schraube_box, gr_schraube_box = schrauben_detection.detect_and_sort_schrauben()
        num = 1;
        for value in s_box:
                if value == 1:
                    value = 0;
                    robot_communication.spitze_sorted(num)
                    num += 1;
                    break;
                else:
                    
                    num += 1;
                    if num > 8:
                         print("Spitzen nachfüllen, sind alle")
        num = 1;
        for value in g_box:
                if value == 1:
                    value = 0;
                    robot_communication.griff_sorted(num)
                    num += 1;
                    break;
                   
                else:
                    num += 1;
                    if num > 8:
                         print("Griff    nachfüllen, sind alle") 

        for value in kl_schraube_box:
                if value == 1:
                    value = 0;
                    robot_communication.kleineSchraube_sorted(num)
                    num += 1;
                    break;
                else:
                    
                    num += 1;
                    if num > 8:
                         print("Spitzen nachfüllen, sind alle")
        num = 1;
        for value in gr_schraube_box:
                if value == 1:
                    value = 0;
                    robot_communication.großeSchraube_sorted(num)
                    num += 1;
                    break;
                else:
                    
                    num += 1;
                    if num > 8:
                         print("Spitzen nachfüllen, sind alle")
        num = 1;
            
        robot_communication.switch(1);
        robot_communication.start_robot_main_task();
# Kamera freigeben und Fenster schließen

if __name__ == "__main__":
    find_position_empty_not_empty()
    cap.release()
    cv2.destroyAllWindows()

    

          