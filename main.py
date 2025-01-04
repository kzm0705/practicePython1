import PySimpleGUI as sg


def main():
    layout = [[sg.Text('hello world')],
              [sg.Button('OK')]]
    
    window = sg.Window('Sample window', layout)

    while True:
        event, values = window.read()

        if event in [sg.WIN_CLOSED, 'OK']:
            break

        window.close()

sample = main()