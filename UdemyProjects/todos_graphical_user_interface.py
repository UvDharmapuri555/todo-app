import functions
import PySimpleGUI as sg
import time

sg.theme("Black")
clock = sg.Text(time.strftime("%B %d, %Y - %T"), key='clock')
label = sg.Text("Enter a todo: ")
input_box = sg.InputText(tooltip="Enter todo here", key="todo")

add_button = sg.Button("Add")
list_box = sg.Listbox(functions.get_todos(), key="todos", enable_events=True, size=(45, 10))
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window("Todo App",
                   layout=[[label], [clock], [input_box, add_button], [list_box, edit_button], [complete_button,
                                                                                                exit_button]],
                   font=('helvetica', 20))
while True:
    event, values = window.read(timeout=10)
    window['clock'].update(value=time.strftime("%B %d, %Y - %T"))
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"].title() + "\n"
            if values['todo'] == '':
                continue
            index = len(values['todos'])
            number_items = f"{index + 1}. {new_todo}"
            new_todo = number_items
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')
        case "Edit":
            try:
                edit_todo = values['todos'][0]
                new_todo = values['todo'].title() + "\n"

                todos = functions.get_todos()
                index = todos.index(edit_todo)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.Popup("Please select an item first!", font=("Helvetica", 20))
        case "Complete":
            try:
                todos = functions.get_todos()
                complete_todo = values["todos"][0]
                index = todos.index(complete_todo)
                todos.pop(int(index))
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.Popup("Please select an item first!", font=("Helvetica", 20))
                continue
        case "Exit":
            break
        case "todos":
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break

window.close()
