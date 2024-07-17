import functions
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
    elif user_action.startswith("show"):
        todos = get_todos(FILE_PATH_NAME)
        for ind, item in enumerate(todos):
            item = item.strip('\n')
            print(ind+1, item)
    elif user_action.startswith("edit"):
        try:
            num = user_action[5:]
            if num.isdigit():
                no = int(num) -1
            else:
                continue

            todos = get_todos(FILE_PATH_NAME)
            new_value = input(f"Provide the new value for {todos[no]}")
            todos[no] = new_value + '\n'
            functions.write_todos(filepath=FILE_PATH_NAME,todos_list=todos)
        except ValueError:
            print("Invalid command")
            continue
        except IndexError:
            print("There is no item with that number.")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid.")

