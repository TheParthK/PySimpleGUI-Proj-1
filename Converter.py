import PySimpleGUI as sg

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

layout = [
    [sg.Text('Converter')],
    [sg.Text('Enter Value : '), sg.Input(key='-INPUT-')],
    [sg.Text('Select Unit From:\t'), sg.Spin(['Kms/hr', 'Miles/hr', 'm/s'], key='-FROM-')],
    [sg.Text('Select Unit To:\t'), sg.Spin(['Kms/hr', 'Miles/hr', 'm/s'], key='-TO-')],
    [sg.Button('Convert', key='-CONVERT-')],
    [sg.Text('', key='-ANS-')]
]

window = sg.Window('Converter', layout)

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

