import time
import pyautogui

def runOrders():
    ordersFile = open("orders.txt", "r")
    rows = ordersFile.read().split("\n")
    ordersFile.close()

    for row in rows:
        first_word = row.split(" ")[0]

        if first_word == "move":
            first_param = int(row.split(" ")[1])
            second_param = int(row.split(" ")[2])
            pyautogui.move(first_param, second_param)
        
        elif first_word == "moveTo":
            first_param = int(row.split(" ")[1])
            second_param = int(row.split(" ")[2])
            pyautogui.moveTo(first_param, second_param)

        elif first_word == "click":
            first_param = str(row.split(" ")[1]).lower()
            pyautogui.click(button = first_param)

        elif first_word == "dragTo":
            first_param = int(row.split(" ")[1])
            second_param = int(row.split(" ")[2])
            pyautogui.dragTo(first_param, second_param)

        elif first_word == "type":
            first_param = row.split("type ")[1]
            pyautogui.typewrite(first_param)

        elif first_word == "hotkey":
            first_param = row.split("type ")[1]
            pyautogui.hotkey(first_param)

        elif first_word == "delay":
            first_param = row.split("type ")[1]
            time.sleep(first_param)
