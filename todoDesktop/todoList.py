import functions
import os
import FreeSimpleGUI as sg
import time

FILE_PATH_NAME = "../files/todos.txt"

if not os.path.exists(FILE_PATH_NAME):
    with open("../files/todos.txt", "w") as file:
        pass

sg.theme("DarkPurple3")

lbl_time = sg.Text('', key="lblClock")
lbl_todo = sg.Text("Type in a to-do")
txt_todo = sg.InputText("Enter todo", key="txtTodo")
btn_add = sg.Button("Add", key="btnAdd")
lst_todos = sg.Listbox(values=functions.get_todos(FILE_PATH_NAME), key="lstTodos", enable_events=True, size=[45,10])
btn_update = sg.Button("Update")
btn_remove = sg.Button("Remove")
btn_exit = sg.Button("Exit")

window = sg.Window("My To-Do App",
                   layout=[
                       [lbl_time],
                       [lbl_todo],
                       [txt_todo, btn_add],
                       [lst_todos,btn_update,btn_remove],
                       [btn_exit]
                   ], font=("Helvetica", 20))

# event = window.read()
# print(event)
##############################
# event, values = window.read()
# print(event)
# print(values)
##############################

while True:
    event, values = window.read(timeout=200)
    if event != sg.WIN_CLOSED:
        window["lblClock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    # event, values = window.read()
    # print(event)
    # print(values)
    match event:
        case sg.WIN_CLOSED:
            break
        case "btnAdd":
            todos = functions.get_todos(FILE_PATH_NAME)
            new_todo = values["txtTodo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos, FILE_PATH_NAME)
            window["lstTodos"].update(values=todos)
        case "lstTodos":
            window["txtTodo"].update(value=values['lstTodos'][0].replace('\n',''))
        case "Update":
            try:
                todo_to_edit = values['lstTodos'][0]
                new_todo = values['txtTodo'] + "\n"
                n = todos.index(todo_to_edit)
                todos[n] = new_todo
                functions.write_todos(todos, FILE_PATH_NAME)
                window['lstTodos'].update(values=todos)
            except IndexError:
                sg.popup("PLease select the item first.", font=("Helvetica", 20))
        case "Remove":
            try:
                todo_to_remove = values['lstTodos'][0]
                todos = functions.get_todos(FILE_PATH_NAME)
                todos.remove(todo_to_remove)
                functions.write_todos(todos,FILE_PATH_NAME)
                window['lstTodos'].update(values=todos)
                window['txtTodo'].update(value='')
            except IndexError:
                sg.popup("PLease select the item first.", font=("Helvetica", 20))
        case "Exit":
            break

print('Bye')
window.close()





