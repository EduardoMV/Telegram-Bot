from time import sleep
from datetime import datetime, time
import pyautogui


def wait_to_start(start_time, action, params):
    interval = 1 #seconds
    intTime = time(*(map(int, start_time.split(":") )))
    nowTime = datetime.today().time()

    while intTime > nowTime:
        intTime = time(*(map(int, start_time.split(":") )))
        nowTime = datetime.today().time()
        sleep(interval)
 
    action(params)
    return action

def open_zoom(room_id):
    pyautogui.hotkey("win")
    pyautogui.typewrite("zoom")
    pyautogui.hotkey("enter")
    print("Estoy abriendo zoom" + room_id)

print("iniciar")
wait_to_start("16:41", open_zoom, "Imorelos")
open_zoom("Imorelos")
print("finalizar")