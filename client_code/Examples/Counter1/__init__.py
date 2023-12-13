import anvil.server
from ._anvil_designer import Counter1Template
from anvil_reactive.main import signal, render_effect, effect

class Counter1(Counter1Template):
    counter = signal(0)

    def __init__(self, **properties):
        self.title_label.text = type(self).__name__
        self.init_components(**properties)

    @render_effect
    def render(self):
        self.label_1.text = self.counter

    def btn_plus_click(self, **event_args):
        self.counter += 1

    def btn_minus_click(self, **event_args):
        self.counter -= 1
    
    