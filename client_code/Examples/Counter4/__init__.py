from ._anvil_designer import Counter4Template
import anvil.server
from anvil.tables import app_tables
from anvil_reactive.main import signal, render_effect, effect, bind, reactive_class, reactive_instance

counter = reactive_instance(app_tables.counter.get())


class Counter4(Counter4Template):
    def __init__(self, **properties):
        self.title_label.text = type(self).__name__
        self.init_components(**properties)

    @render_effect
    def render(self):
        self.label_1.text = counter["value"]

    def btn_plus_click(self, **event_args):
        anvil.server.call('update_counter', counter, 1)

    def btn_minus_click(self, **event_args):
        anvil.server.call('update_counter', counter, -1)
        print(counter["value"])
