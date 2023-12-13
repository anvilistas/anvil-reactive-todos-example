from ._anvil_designer import Writeback3Template
from anvil_reactive.main import signal, render_effect

class Writeback3(Writeback3Template):
    """same as Writeback1 but without bind/writeback"""
    text = signal("")

    def __init__(self, **properties):
        self.init_components(**properties)

    @render_effect
    def update_text(self):
        self.text_box_1.text = self.text
        self.label_1.text = self.text

    def clear_button_click(self, **event_args):
        self.text = ""

    def text_box_1_change(self, **event_args):
        self.text = self.text_box_1.text
