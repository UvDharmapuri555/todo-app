import functions
import PySimpleGUI as sg

label = sg.Text("Enter a todo: ")
input_box = sg.InputText(tooltip="Enter todo here", key="todo")

add_button = sg.Button("Add")
list_box = sg.Listbox(functions.get_todos(), key="todos", enable_events=True, size=(45, 10))
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")

window = sg.Window("Todo App",
                   layout=[[label], [input_box, add_button], [complete_button], [list_box, edit_button]],
                   font=('helvetica', 20))
while True:
    event, values = window.read()
    print(event)
    print(values)
    print(values['todos'])
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            if values['todo'] == '':
                continue
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')
        case "Edit":
            edit_todo = values['todos'][0]
            new_todo = values['todo'] + "\n"

            todos = functions.get_todos()
            index = todos.index(edit_todo)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')
        case "Complete":
            todos = functions.get_todos()
            complete_todo = values["todos"][0]
            index = todos.index(complete_todo)
            todos.pop(int(index))
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')
        case "todos":
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break

window.close()
