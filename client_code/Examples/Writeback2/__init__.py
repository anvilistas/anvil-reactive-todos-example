from ._anvil_designer import Writeback2Template
from anvil_reactive.main import writeback, signal, bind

class Writeback2(Writeback2Template):
    """Same as Writeback1 but with getters and setters"""
    text = signal("")
    def __init__(self, **properties):
        self.init_components(**properties)
        writeback(self.text_box_1, "text", self.get_text, self.set_text, ["change"])
        # writeback(self.text_box_1, "text", lambda: self.text, lambda v: setattr(self, "text", v), ["change"])
        bind(self.label_1, "text", lambda: self.text)

    def get_text(self):
        return self.text

    def set_text(self, v):
        self.text = v

    def clear_button_click(self, **event_args):
        self.text = ""
