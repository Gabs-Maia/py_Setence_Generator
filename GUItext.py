# gui.py
import PySimpleGUI as sg



def create_gui():
    # Layout definition 
    layout = [
        [sg.Text("Enter the file path:")],
        [sg.Input(key="-INPUT-")],
        [sg.Button("Run"), sg.Button("Exit")],
        [sg.Output(size=(80, 20))]
    ]

    # Window app creation
    window = sg.Window("PDF Text Formater", layout)
   
    while True:
    # Call the GUI function 
        window = gui.create_gui()
        event, values = window.read()
    # End program 
        if event == sg.WINDOW_CLOSED or event == "Exit":

            break
    # Run code if user presses button
        elif event == "Run":
            input_path = values["-INPUT-"]
    
    return window