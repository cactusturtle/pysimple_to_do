import PySimpleGUI as sg
# Set Program Theme
sg.theme('LightTeal')

# Set up the layout
layout = [
    [sg.Checkbox(''), sg.T('1.'), sg.In(key=1)],
    [sg.Checkbox(''), sg.T('2.'), sg.In(key=2)],
    [sg.Checkbox(''), sg.T('3.'), sg.In(key=3)],
    [sg.Checkbox(''), sg.T('4.'), sg.In(key=4)],
    [sg.Button('Exit')]
]

# Set up the window
window = sg.Window('To Do', layout)

# Listen for Window Close
while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED() or event == 'Exit':
        break

window.close()