from ._anvil_designer import Writeback1Template
from anvil_reactive.main import writeback, signal, bind

class Writeback1(Writeback1Template):
    text = signal("")
    def __init__(self, **properties):
        self.init_components(**properties)
        writeback(self.text_box_1, "text", self, "text", ["change"])
        bind(self.label_1, "text", self, "text")

    def clear_button_click(self, **event_args):
        self.text = ""

