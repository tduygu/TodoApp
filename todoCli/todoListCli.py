from functions import get_todos, write_todos
import time

FILE_PATH_NAME = "../files/todos.txt"

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:] + "\n"
        todos = get_todos(FILE_PATH_NAME)
        todos.append(todo)
        write_todos(filepath=FILE_PATH_NAME, todos_list=todos)
    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid.")

