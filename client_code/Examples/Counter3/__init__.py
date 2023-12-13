import anvil.server
from ._anvil_designer import Counter3Template
from anvil_reactive.main import signal, render_effect, effect, bind, reactive_class

@reactive_class
class Counter3(Counter3Template):
    def __init__(self, **properties):
        self.counter = 0
        self.title_label.text = type(self).__name__
        self.init_components(**properties)

    @render_effect
    def render(self):
        self.label_1.text = self.counter

    def btn_plus_click(self, **event_args):
        self.counter += 1

    def btn_minus_click(self, **event_args):
        self.counter -= 1
