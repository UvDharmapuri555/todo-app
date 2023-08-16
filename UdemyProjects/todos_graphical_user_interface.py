import functions
import PySimpleGUI as sg

label = sg.Text("Enter a todo: ")
input_box = sg.InputText(tooltip="Enter todo here")

add_button = sg.Button("Add")

window = sg.Window("Todo App", layout=[[label], [input_box, add_button]])
window.read()
window.close()