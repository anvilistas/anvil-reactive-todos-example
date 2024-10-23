from anvil_reactive.main import reactive_class, effect
from anvil_extras.storage import indexed_db
from uuid import uuid4

todos_db = indexed_db

from anvil_reactive.main import reactive_list
from anvil_reactive.main._computations import StoreSignal

lt = StoreSignal.__lt__

def __lt__(self, other):
    print(self, other)
    return lt(self, other)

StoreSignal.__lt__ = lt

def sort(self, *args, **kws):
    debugger
    rv = list.sort(self, *args, **kws)
    self.LIST_LEN.update()
    return rv

# reactive_list.sort = sort

@reactive_class
class TodoStore:
    def __init__(self):
        self.todos = todos_db.get("todos", [])

    def add_todo(self, description):
        self.todos.append({"id": str(uuid4()), "description": description, "completed": False})

    def toggle_complete(self, todo):
        todo["completed"] = not todo["completed"]

    def delete_todo(self, todo):
        # self.todos.remove(todo)
        # self.todos.sort(key=lambda v: v["description"])
        self.todos.sort()

    @effect
    def save_todos(self):
        print("saving todos")
        todos_db["todos"] = [dict(todo) for todo in self.todos]


todo_store = TodoStore()