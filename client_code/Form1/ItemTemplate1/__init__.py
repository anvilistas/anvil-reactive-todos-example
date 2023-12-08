from ._anvil_designer import ItemTemplate1Template
from anvil import *
from anvil_reactive.main import render_effect
from anvil.js import get_dom_node
from ...Todos import todo_store

class ItemTemplate1(ItemTemplate1Template):
    def __init__(self, **properties):
        self.init_components(**properties)

    @render_effect
    def set_icon(self):
        self.todo_description.text = self.item["description"]
        label_node = get_dom_node(self.todo_description).querySelector("span")
        if self.item["completed"]:
            self.toggle_todo.icon = "fa:check-circle-o"
            label_node.style.textDecoration = "line-through"
        else:
            self.toggle_todo.icon = "fa:circle-o"
            label_node.style.textDecoration = ""

    def toggle_todo_click(self, **event_args):
        todo_store.toggle_complete(self.item)

    def delete_todo_click(self, **event_args):
        todo_store.delete_todo(self.item)
