import PySimpleGUI as sg
from numpy import pad, size

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False



layout = [
    [sg.Text('Converter', font=('Phosphate', 25), size=(10, 2))],
    [sg.Text('Enter Value:\t', font=('Big Caslon', 17)), sg.Input(key='-INPUT-', size=(9, 1), font=('Big Caslon', 17))],
    [sg.Text('Select Unit From:\t', font=('Big Caslon', 17)), sg.Spin(['Kms/hr', 'Miles/hr', 'm/s'], key='-FROM-', font=('Big Caslon', 17), size=(8, 1))],
    [sg.Text('Select Unit To:\t', font=('Big Caslon', 17)), sg.Spin(['Kms/hr', 'Miles/hr', 'm/s'], key='-TO-', font=('Big Caslon', 17), size=(8, 1))],
    [sg.Button('Convert', key='-CONVERT-', font=('Big Caslon', 17))],
    [sg.Text('', key='-ANS-', font=('Big Caslon', 17))]
]

window = sg.Window('Converter', layout, margins=(10, 10))

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    f = values['-FROM-']
    t = values['-TO-']
    a = ''
    k = 'Kms/hr'
    mile = 'Miles/hr'
    m = 'm/s'
    if event == '-CONVERT-':
        inp = values['-INPUT-']
        if isfloat(inp):
            if f == k:
                if t == k:
                    a = inp + ' Km/h = ' + inp + ' Km/h'
                elif t == mile:
                    a = 0.621371 * float(inp)
                    a = round(a, 2)
                    a = inp + ' Km/h = ' + str(a) + ' mph'
                elif t == m:
                    a = 0.277778 * float(inp)
                    a = round(a, 2)
                    a = inp + ' Km/h = ' + str(a) + ' m/s'
            elif f == mile:
                if t == mile:
                    a = inp + ' mph = ' + inp + ' mph'
                elif t == k:
                    a = 1.60934 * float(inp)
                    a = round(a, 2)
                    a = inp + ' mph = ' + str(a) + ' Km/h'
                elif t == m:
                    a = 0.44704 * float(inp)
                    a = round(a, 2)
                    a = inp + ' mph = ' + str(a) + ' m/s'
            elif f == m:
                if t == m:
                    a = inp + ' m/s = ' + inp + ' m/s'
                elif t == k:
                    a = 3.6 * float(inp)
                    a = round(a, 2)
                    a = inp + ' m/s = ' + str(a) + ' Km/h'
                elif t == mile:
                    a = 2.23694 * float(inp)
                    a = round(a, 2)
                    a = inp + ' m/s = ' + str(a) + ' mph'
        else:
            a = '[ERROR #1]: Invalid Data Type'

        window['-ANS-'].update(a)

window.close()
