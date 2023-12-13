import anvil.server
from ._anvil_designer import Counter2Template
from anvil_reactive.main import signal, render_effect, effect, bind

class Counter2(Counter2Template):
    counter = signal(0)

    def __init__(self, **properties):
        bind(self.label_1, "text", lambda: self.counter)
        self.title_label.text = type(self).__name__

    def btn_plus_click(self, **event_args):
        self.counter += 1

    def btn_minus_click(self, **event_args):
        self.counter -= 1
