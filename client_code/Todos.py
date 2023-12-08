from anvil_reactive import reactive_class
from anvil_extras.storage import indexed_db

todos_db = indexed_db.create()

@reactive_class
class TodoStore:
    def __init__(self):
        pass