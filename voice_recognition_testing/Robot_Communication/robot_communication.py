from asyncio import wait
import requests
from requests.auth import HTTPDigestAuth


IP = "192.168.125.1"  
PORT = 80

USERNAME = 'Default User'
PASSWORD = 'robotics'


session = requests.Session()
session.auth = HTTPDigestAuth(USERNAME, PASSWORD)


def set_execution_cycle(cycle_mode: str) -> None:
    """
    Sendet einen POST-Befehl an den Roboter, um den RAPID Execution Cycle zu setzen.
    Args:
        cycle_mode (str): Wähle zwischen "once" (einmalige Ausführung) oder "forever" (kontinuierliche Ausführung).
    """
    if cycle_mode not in ["once", "forever"]:
        print("Fehler: Ungültiger Wert für cycle_mode. Verwende 'once' oder 'forever'.")
        return

    response = session.post(f"http://{IP}:{PORT}/rw/rapid/execution?action=setcycle",
                             data={"cycle": cycle_mode},
                             auth=HTTPDigestAuth(USERNAME, PASSWORD))
    
    if response.status_code == 204:
        print(f"Execution Cycle erfolgreich auf '{cycle_mode}' gesetzt.")
    else:
        print(f"Fehler {response.status_code}: {response.text}")




def spitze_sorted(position: int) -> None:
    """
    Setzt die entsprechende spitzeX Variable in RAPID auf 1.

    Args:
        position (int): Die Position der Spitze (1 bis 8).
    """
    if position < 1 or position > 8:
        print("Fehler: Die Position muss zwischen 1 und 8 liegen!")
        return

    url = f"http://{IP}:{PORT}/rw/rapid/symbol/data/RAPID/T_ROB_L/MainModule/spitze{position}?action=set"
    data = {"value": "1"}

    try:
        response = session.post(url, data=data, auth=HTTPDigestAuth(USERNAME, PASSWORD))
        if response.status_code == 204:
            print(f"✅ spitze{position} erfolgreich auf 1 gesetzt!")
        else:
            print(f"⚠️ Fehler beim Setzen von spitze{position}: {response.status_code} - {response.text}")
    except requests.RequestException as e:
        print(f"🚨 Netzwerkfehler: {e}")











def modi_R(input_value: int) -> None:
  
    response = session.post(f"http://{IP}:{PORT}/rw/rapid/symbol/data/RAPID/T_ROB_R/MainModule/auto?action=set",
                            data={"value": str(input_value)},
                            auth=HTTPDigestAuth(username='Default User',
                            password='robotics'))
    pass

def modi_L(input_value: int) -> None:
  
    response = session.post(f"http://{IP}:{PORT}/rw/rapid/symbol/data/RAPID/T_ROB_L/MainModule/auto?action=set",
                            data={"value": str(input_value)},
                            auth=HTTPDigestAuth(username='Default User',
                            password='robotics'))
    pass



def griff_sorted(position: int) -> None:
    """
    Setzt die entsprechende griffX Variable in RAPID auf 1.

    Args:
        position (int): Die Position des Griffs (1 bis 8).
    """
    if position < 1 or position > 8:
        print("Fehler: Die Position muss zwischen 1 und 8 liegen!")
        return

    url = f"http://{IP}:{PORT}/rw/rapid/symbol/data/RAPID/T_ROB_L/MainModule/griff{position}?action=set"
    data = {"value": "1"}

    try:
        response = session.post(url, data=data, auth=HTTPDigestAuth(USERNAME, PASSWORD))
        if response.status_code == 204:
            print(f"✅ griff{position} erfolgreich auf 1 gesetzt!")
        else:
            print(f"⚠️ Fehler beim Setzen von griff{position}: {response.status_code} - {response.text}")
    except requests.RequestException as e:
        print(f"🚨 Netzwerkfehler: {e}")

def kleineSchraube_sorted(position: int) -> None:
    """
    Setzt die entsprechende kleineSchraubeX Variable in RAPID auf 1.

    Args:
        position (int): Die Position der kleinen Schraube (1 bis 8).
    """
    if position < 1 or position > 8:
        print("Fehler: Die Position muss zwischen 1 und 8 liegen!")
        return

    url = f"http://{IP}:{PORT}/rw/rapid/symbol/data/RAPID/T_ROB_R/MainModule/kleineSchraube{position}?action=set"
    data = {"value": "1"}

    try:
        response = session.post(url, data=data, auth=HTTPDigestAuth(USERNAME, PASSWORD))
        if response.status_code == 204:
            print(f"✅ kleineSchraube{position} erfolgreich auf 1 gesetzt!")
        else:
            print(f"⚠️ Fehler beim Setzen von kleineSchraube{position}: {response.status_code} - {response.text}")
    except requests.RequestException as e:
        print(f"🚨 Netzwerkfehler: {e}")

def großeSchraube_sorted(position: int) -> None:
    """
    Setzt die entsprechende großeSchraubeX Variable in RAPID auf 1.

    Args:
        position (int): Die Position der großen Schraube (1 bis 8).
    """
    if position < 1 or position > 8:
        print("Fehler: Die Position muss zwischen 1 und 8 liegen!")
        return

    url = f"http://{IP}:{PORT}/rw/rapid/symbol/data/RAPID/T_ROB_R/MainModule/großeSchraube{position}?action=set"
    data = {"value": "1"}

    try:
        response = session.post(url, data=data, auth=HTTPDigestAuth(USERNAME, PASSWORD))
        if response.status_code == 204:
            print(f"✅ großeSchraube{position} erfolgreich auf 1 gesetzt!")
        else:
            print(f"⚠️ Fehler beim Setzen von großeSchraube{position}: {response.status_code} - {response.text}")
    except requests.RequestException as e:
        print(f"🚨 Netzwerkfehler: {e}")


def start_robot_main_task() -> None:
    """
    Sendet eine HTTP POST-Anfrage, um das Hauptprogramm des Roboters in RAPID zu starten.
    """
    response = session.post(
        f"http://{IP}:{PORT}/rw/rapid/execution?action=start",
        data={
            "regain": "continue",
            "execmode": "continue",
            "cycle": "once",
            "condition": "none",
            "stopatbp": "disabled",
            "alltaskbytsp": "false",
        },
        auth=HTTPDigestAuth(username=USERNAME, password=PASSWORD)
    )
    if response.status_code == 204:
        print("Hauptprogramm des Roboters erfolgreich gestartet.")
    else:
        print(f"Fehler beim Starten des Hauptprogramms: {response.status_code}")
        print(f"Antwort: {response.text}")

def stop_robot_main_task() -> None:
    """
    Sendet eine HTTP POST-Anfrage, um das Hauptprogramm des Roboters in RAPID zu starten.
    """
    response = session.post(
        f"http://{IP}:{PORT}/rw/rapid/execution?action=stop",
        data={
            "regain": "continue",
            "execmode": "continue",
            "cycle": "once",
            "condition": "none",
            "stopatbp": "disabled",
            "alltaskbytsp": "false",
        },
        auth=HTTPDigestAuth(username=USERNAME, password=PASSWORD)
    )
    if response.status_code == 204:
        print("Hauptprogramm des Roboters erfolgreich gestartet.")
    else:
        print(f"Fehler beim Starten des Hauptprogramms: {response.status_code}")
        print(f"Antwort: {response.text}")


def set_action_L( input_value: int):
     response = session.post(f"http://{IP}:{PORT}/rw/rapid/symbol/data/RAPID/T_ROB_L/MainModule/action?action=set",
                            data={"value": str(input_value)},
                            auth=HTTPDigestAuth(username='Default User',
                            password='robotics'))
def set_action_R( input_value: int):
     response = session.post(f"http://{IP}:{PORT}/rw/rapid/symbol/data/RAPID/T_ROB_R/MainModule/action?action=set",
                            data={"value": str(input_value)},
                            auth=HTTPDigestAuth(username='Default User',
                            password='robotics'))


def switch(mod):
    if mod == 0:
        modi_L(0)
        modi_R(0)
    if mod == 1:
        modi_L(1)
        modi_R(1)


def open_gripper_L():
    switch(0);
    set_action_L(3);
    start_robot_main_task();

def close_gripper_L():
    switch(0);
    set_action_L(4);
    start_robot_main_task();


def open_gripper_R():
    switch(0);
    set_action_R(3);
    start_robot_main_task();

def drop_griff():
    switch(0);
    set_action_L(1)
    start_robot_main_task();

def drop_kl_schraube():
    switch(0);
    set_action_R(1)
    start_robot_main_task();

def drop_gr_schraube():
    switch(0);
    set_action_R(2)
    start_robot_main_task();

def drop_spitze():
    switch(0);
    set_action_L(2)
    start_robot_main_task();

def give_griff():
    switch(0);
    set_action_L(5)
    start_robot_main_task();

def give_spitze():
    switch(0);
    set_action_L(6);
    start_robot_main_task();
def give_kl_schraube():
    switch(0);
    set_action_R(5);
    start_robot_main_task();
def give_gr_schraube():
    switch(0);
    set_action_R(6);
    start_robot_main_task();








