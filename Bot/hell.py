#python -m pip install pysimplegui
import PySimpleGUI as sg
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

def main():

    sg.theme('DarkBrown4')
    layout = [ [sg.Text("Welcome to hell human")], [sg.Text("Enter your name"),sg.InputText()], [sg.Button("OK 3"),sg.Button("Cancel")], [sg.Input(do_not_clear=False)] ]
    window = sg.Window("Hell.exe", layout)

    while True:
        event, values = window.read()
        if event == "OK 3": #(or event == sg.WIN_CLOSED:)
            break
        elif event == "Cancel":
            runOrders()
        elif event == sg.WIN_CLOSED:
            layout = [ [sg.Text("Finally giving up? Give me your name")], [sg.InputText()], [sg.Button("GIVE UP ON HOPE")], [sg.Input(do_not_clear=False)] ]
            window = sg.Window("Hell.exe", layout)     
            


    window.close()
    
main()