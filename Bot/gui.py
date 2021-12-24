#python -m pip install pysimplegui
import PySimpleGUI as sg
import pyautogui

def runOrders():
    ordersFile = open("orders.txt", "r")
    currentTasks = ordersFile.read().split("\n")
    ordersFile.close()

    for row in currentTasks:
        first_word = row.split(" ")[0]

        if first_word == "move":
            first_param = int(row.split(" ")[1])
            second_param = int(row.split(" ")[2])
            pyautogui.move( first_param, second_param)

        elif first_word == "moveTo":
            first_param = int(row.split(" ")[1])
            second_param = int(row.split(" ")[2])
            pyautogui.moveTo( first_param, second_param)

        elif first_word == "click":
            first_param = str(row.split(" ")[1]).lower()
            pyautogui.click( button=first_param )

        elif first_word == "dragTo":
            first_param = int(row.split(" ")[1])
            second_param = int(row.split(" ")[2])
            pyautogui.dragTo( first_param, second_param)

        elif first_word == "type":
            first_param = row.split("type ")[1]
            pyautogui.typewrite( first_param )

def main():
    ordersFile = open("orders.txt", "r")
    currentTasks = ordersFile.read().split("\n")
    ordersFile.close()

    validCommands = [
        "click",
        "dragTo",
        "move",
        "moveTo",
        "type"
    ]
    validCommandsCombo = sg.Combo(key="VALIDCOMMANDS_COMBO", values = ( validCommands ), size=(10,1), enable_events=True)

    
    inputTextA = sg.InputText(key="FIRSTPARAM_INPUT", do_not_clear=False, visible=True, size=(50,1))
    inputTextB = sg.InputText(key="SECONDPARAM_INPUT", do_not_clear=False, visible=False, size=(50,1))

    layout = [ 
        [ sg.Text("AUTOBOT", justification="center", font=("Helvetica", 35), text_color="black", size=(20, 1)) ],
        [ 
            sg.Button("LOAD", size=(7, 1), font=("Helvetica", 15), button_color=("white", "#218fef")),
            sg.Button("SAVE", size=(7, 1), font=("Helvetica", 15), button_color=("white", "#57b73c")),
            sg.Button("RUN", size=(7, 1), font=("Helvetica", 15), button_color=("white", "#57b73c")),
            sg.Button("CLOSE", size=(7, 1), font=("Helvetica", 15), button_color=("white", "#d62020")),
            sg.Text("x = 1500", font=("Helvetica", 12), size=(7, 1), key="TEXT_X_COORDINATE"),
            sg.Text("y = 500", font=("Helvetica", 12), size=(7, 1), key="TEXT_Y_COORDINATE")
        ],
        [ sg.Text("Your tasks are:", font=("Helvetica", 12), text_color="black", size=(13, 1)) ],
        [ sg.Listbox(key="TASKS_LISTBOX", values = ( currentTasks ), size=(60,5)) ],
        [
            sg.Button("UP", size=(7, 1)),
            sg.Button("DOWN", size=(7, 1)),
            sg.Button("DELETE", button_color=("white", "#d62020"))
        ],
        [
            validCommandsCombo,
            inputTextA,
            sg.Button("ADD")
        ],
        [
            inputTextB
        ]
    ]

    window = sg.Window(
        "Autobot GUI",
        auto_size_text=False,
        auto_size_buttons=False,
        no_titlebar=False,
        grab_anywhere=True, #Window is easier to drag
        return_keyboard_events=False, #In case you want to create shorcuts like ctrl + S 
        keep_on_top=False, #If you keep this windows on the top you cannot click some elements
        background_color='gray',
        location=(720, 390),
        layout=layout)

    while True:
        event, values = window.read()

        if event == "LOAD":
            #
            print("Button LOAD was clicked")
            #
        elif event == "SAVE":
            #
            print("Button SAVE was clicked")
            #
        elif event == "RUN":
            #
            print("Button RUN was clicked")
            #
        elif event == "CLOSE" or event == sg.WIN_CLOSED:
            break

    
        elif event == "UP":
            try:
                search = values["TASKS_LISTBOX"][0]
                indexToDelete = currentTasks.index( search )

                if indexToDelete > 0:
                    taskToMove = currentTasks[ indexToDelete ]
                    currentTasks.pop( indexToDelete )
                    currentTasks.insert( indexToDelete - 1, taskToMove)

                    window.FindElement("TASKS_LISTBOX").update( values = currentTasks )
            except:
                sg.popup_auto_close("No element selected", no_titlebar=True)


        elif event == "DOWN":
            try:
                search = values["TASKS_LISTBOX"][0]
                indexToDelete = currentTasks.index( search )

                if indexToDelete <= len(currentTasks) - 1:
                    taskToMove = currentTasks[ indexToDelete ]
                    currentTasks.pop( indexToDelete )
                    currentTasks.insert( indexToDelete + 1, taskToMove)

                    window.FindElement("TASKS_LISTBOX").update( values = currentTasks )
            except:
                sg.popup_auto_close("No element selected", no_titlebar=True)


        elif event == "DELETE":
            search = values["TASKS_LISTBOX"][0]
            indexToDelete = currentTasks.index( search )
            currentTasks.pop( indexToDelete )

            currentIndex = 1
            for task in currentTasks:
                spaceIndex = task.find( " " )
                numberList = task[0:spaceIndex]
                task.replace( numberList, "", 1)
                task = str(currentIndex) + task
                #currentTasks[currentIndex - 1] = task
                currentIndex += 1                

            window.FindElement("TASKS_LISTBOX").update( values = currentTasks)

        elif event == "ADD":
            new_id = len(currentTasks) + 1

            new_task = str(new_id) + " " + values["VALIDCOMMANDS_COMBO"] + " " + values["FIRSTPARAM_INPUT"] + " " + values["SECONDPARAM_INPUT"]
            currentTasks.append( new_task )
            currentIndex = 1
            for task in currentTasks:
                spaceIndex = task.find( " " )
                numberList = task[0:spaceIndex]
                task.replace( numberList, "", 1)
                task = str(currentIndex) + task
                currentIndex += 1   

            window.FindElement("TASKS_LISTBOX").update( values = currentTasks)

        elif event == "VALIDCOMMANDS_COMBO":
            if values["VALIDCOMMANDS_COMBO"] == "click":
                window.FindElement("SECONDPARAM_INPUT").update( visible=False )

            elif values["VALIDCOMMANDS_COMBO"] == "dragTo":
                window.FindElement("SECONDPARAM_INPUT").update( visible=True )

            elif values["VALIDCOMMANDS_COMBO"] == "move":
                window.FindElement("SECONDPARAM_INPUT").update( visible=True )

            elif values["VALIDCOMMANDS_COMBO"] == "moveTo":
                window.FindElement("SECONDPARAM_INPUT").update( visible=True )

            elif values["VALIDCOMMANDS_COMBO"] == "type":
                window.FindElement("SECONDPARAM_INPUT").update( visible=False )

    window.close()

main()