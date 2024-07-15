import functions
import os
import FreeSimpleGUI as sg
import time

if not os.path.exists("../files/todos.txt"):
    with open("../files/todos.txt", "w") as file:
        pass

sg.theme("DarkPurple3")

lbl_time = sg.Text('', key="lbl_clock")
lbl_todo = sg.Text("Type in a to-do")
txt_todo = sg.InputText("Enter todo", key="txtTodo")
btn_add = sg.Button("Add", key="btnAdd")
lst_todos = sg.Listbox(values=functions.get_todos("../files/todos.txt"), key="lstTodos", enable_events=True, size=[45,10])
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

event = window.read()
print(event)

