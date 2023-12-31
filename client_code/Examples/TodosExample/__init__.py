from ._anvil_designer import TodosExampleTemplate
from .TodosStore import todo_store
from anvil_reactive.main import render_effect

class TodosExample(TodosExampleTemplate):
    def __init__(self, **properties):
        self.init_components(**properties)

    def add_todo(self, **event_args):
        description = self.new_todo_input.text
        if description:
            self.new_todo_input.text = ""
            todo_store.add_todo(description)

    @render_effect
    def set_items(self):
        self.todos_panel.items = todo_store.todos
