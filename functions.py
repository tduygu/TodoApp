FILEPATH = "files/todos.txt"

def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of
    to-do items.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_list, filepath=FILEPATH):
    """ Write the to-do items list in a text file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_list)


# You want these lines be executed only when functions.py is directly executed
# and want these lines not to be executed when functions.py is imported
# so:

if __name__ == '__main__':
    # print("Hello from functions")
    print(help(get_todos))
    print(help(write_todos))
    # print(get_todos())


# print(__name__)