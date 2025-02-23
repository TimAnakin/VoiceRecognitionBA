import time
from Model_testing import give_griff,get_griff_into_halterung,get_spitze_into_halterung,give_spitze,automodus,check_spitze,check_count_spitze,check_griff,check_count_griff
from Robot_Communication import robot_communication
from schrauben_detection import get_gr_schraube_into_halterung,get_kl_schraube_into_halterung,check_count_gr_schraube,check_count_kl_schraube,check_gr_schraube,check_kl_schraube, give_gr_schraube, give_kl_schraube
class IntentHandler:
    def __init__(self):
        self.steps_executed = []  # Nachverfolgung der ausgeführten Schritte
        self.mode = None 
        print("Initialisiert")


    def handle_intent(self, intent, *args, **kwargs):

        intent_methods = {
    "arbeitsmodus": self.set_arbeitsmodus,
    "check_count_große_schraube": self.check_count_grosse_schraube,
    "check_count_kleine_schraube": self.check_count_kleine_schraube,
    "check_count_oberteil": self.check_count_oberteil_und_griff,
    "check_count_spitze": self.check_count_spitze,
    "check_griff": self.check_griff,
    "check_große_schraube": self.check_grosse_schraube,
    "check_kleine_schraube": self.check_kleine_schraube,
    "check_spitze": self.check_spitze,
    "drop_griff": self.drop_grip_or_top_into_holder,
    "drop_große_schraube": self.drop_large_screws_into_holder,
    "drop_kleine_schraube": self.drop_small_screws_into_holder,
    "drop_spitze": self.drop_tip_or_bottom_into_holder,
    "give_griff": self.give_griff,
    "give_große_schraube": self.give_large_screw,
    "give_kleine_schraube": self.give_small_screw,
    "give_tip_or_bottom": self.give_tip_or_bottom,
    "open_linken_greifer": self.open_left,
    "open_rechten_greifer": self.open_right,
    "do_next_step": self.do_next_step,
    "offener_modus": self.set_offener_modus,
    "schraube": self.schraube,
    "start_application": self.start_application,
    "stop_application": self.stopp_application,
    "tell_next_step": self.determine_next_step
}

        if intent in intent_methods:
            return intent_methods[intent](*args, **kwargs)
        else:
            raise ValueError(f"Unknown intent: {intent}")
        
    def set_offener_modus(self):
        self.mode = "offener_modus"
        self.stopp_application();
        return "Offener Modus wurde aktiviert."
    def schraube(self):
        print('Welche Schraube soll wohin gebracht werden?')
    def set_arbeitsmodus(self):
        self.mode = "arbeitsmodus"

        timer_set(10," Bis der Arbeitsmodus beginnt...⏳")
        automodus()
    # Methoden für die Intents
    def check_griff(self):
        if check_griff():
            print("Es sind noch Griffe vorhanden")
        else:
            print("Es sind keine mehr vorhanden ")

    def check_spitze(self):
        if check_spitze():
            print("Es sind noch Spitzen vorhanden")
        else:
            print("Es sind keine mehr vorhanden ")

    def check_count_spitze(self):
        num = check_count_spitze();
        print ("Es sind noch "+ str(num) +" Spitzen vorhanden")

    def next_step(self):
        # Kontextbasierte Logik für den nächsten Schritt
        return self.determine_next_step()

    def check_count_oberteil_und_griff(self):
        num = check_count_griff();
        print ("Es sind noch "+ str(num) +" Griffe vorhanden")

    def check_kleine_schraube(self):
        if check_kl_schraube():
            print("Es sind noch kleine Schrauben vorhanden")
        else:
            print("Es sind keine mehr vorhanden ")

    def check_grosse_schraube(self):
        if check_gr_schraube():
            print("Es sind noch große Schrauben vorhanden")
        else:
            print("Es sind keine mehr vorhanden ")

    def open_right(self):
        return robot_communication.open_gripper_L()

    def open_left(self):
        return robot_communication.open_gripper_R()

    def check_count_kleine_schraube(self):
        num = check_count_kl_schraube();
        print ("Es sind noch "+ str(num) +" kleine Schrauben vorhanden")

    def check_count_grosse_schraube(self):
        num = check_count_gr_schraube();
        print ("Es sind noch "+ str(num) +" große Schrauben vorhanden")

    def give_small_screw(self):
        give_kl_schraube()

    def give_large_screw(self):
        give_gr_schraube()

    def give_griff(self):
        give_griff();
       

    def give_tip_or_bottom(self):
        give_spitze();

    def start_application(self):
         robot_communication.start_robot_main_task()

    def stopp_application(self):
         robot_communication.stop_robot_main_task()

    def drop_tip_or_bottom_into_holder(self):
        self.steps_executed.append("drop_tip_or_bottom_into_holder")
        get_spitze_into_halterung();
    
    
    def drop_small_screws_into_holder(self):
        self.steps_executed.append("drop_small_screws_into_holder")
        get_kl_schraube_into_halterung();

    def drop_large_screws_into_holder(self):
        self.steps_executed.append("drop_large_screws_into_holder")
        get_gr_schraube_into_halterung();
    
    def drop_grip_or_top_into_holder(self):
        self.steps_executed.append("drop_grip_or_top_into_holder")
        print("Wird erledigt")
        get_griff_into_halterung();
        
        

    def do_next_step(self):
        # Reihenfolgebasierte Logik für den nächsten Schritt
        steps = [
            "drop_tip_or_bottom_into_holder",
            "drop_small_screws_into_holder",
            "drop_large_screws_into_holder",
            "drop_grip_or_top_into_holder"
        ]
        for step in steps:
            if step not in self.steps_executed:
                return self.handle_intent(step)
        self.steps_executed = []
        self.handle_intent("drop_tip_or_bottom_into_holder")
        


    def determine_next_step(self):
        steps = [
            "drop_tip_or_bottom_into_holder",
            "drop_small_screws_into_holder",
            "drop_large_screws_into_holder",
            "drop_grip_or_top_into_holder"]
         
        for step in steps:
            if step not in self.steps_executed:
                print("Als nächstes mache" + step)
        return "Next step determined based on context."


def timer_set(wait_time,msg):
    for i in range(wait_time, 0, -1):
        print(f"⏳ {i} {msg}", end="\r")  # Zeigt die Zeit in einer Zeile an
        time.sleep(1)


