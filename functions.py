FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """Read the text file and return the list of the to-do items"""
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_args, filepath=FILEPATH):
    """Write the updated list of items on a text file"""
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_args)
