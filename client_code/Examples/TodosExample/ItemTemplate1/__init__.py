from ._anvil_designer import ItemTemplate1Template
from anvil_reactive.main import render_effect
from anvil.js import get_dom_node
from ..TodosStore import todo_store

class ItemTemplate1(ItemTemplate1Template):
    def __init__(self, **properties):
        self.init_components(**properties)
        self.label_node = get_dom_node(self.todo_description).querySelector("span")

    @render_effect
    def render_todo(self):
        self.todo_description.text = self.item["description"]
        if self.item["completed"]:
            self.toggle_todo.icon = "fa:check-circle-o"
            self.label_node.style.textDecoration = "line-through"
        else:
            self.toggle_todo.icon = "fa:circle-o"
            self.label_node.style.textDecoration = ""

    def toggle_todo_click(self, **event_args):
        todo_store.toggle_complete(self.item)

    def delete_todo_click(self, **event_args):
        todo_store.delete_todo(self.item)
