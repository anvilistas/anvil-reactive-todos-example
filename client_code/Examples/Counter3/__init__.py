from ._anvil_designer import Counter3Template
from anvil_reactive.main import signal, render_effect, effect, bind, reactive_class, writeback

@reactive_class
class Counter3(Counter3Template):
    def __init__(self, **properties):
        self.counter = 0
        self.title_label.text = type(self).__name__
        self.foo = self.counter
        writeback(self, "counter", self, "foo", "x-change")
        
        self.init_components(**properties)

    @render_effect
    def render(self):
        self.label_1.text = self.counter


    def btn_plus_click(self, **event_args):
        self.counter += 1
        self.raise_event("x-change")

    def btn_minus_click(self, **event_args):
        self.counter -= 1
        self.raise_event("x-change")

    def button_1_click(self, **event_args):
        """This method is called when the button is clicked"""
        self.foo *= 2
        # self.raise_event("x-change")

