from ._anvil_designer import CustomComponentTemplate
from anvil import *
from anvil_reactive.main import signal, bind, writeback, render_effect


class CustomComponent(CustomComponentTemplate):
    value = signal(0)

    def __init__(self, **properties):
        self.init_components(**properties)
        bind(self.progress_circle_1, "value", self, "value")
        writeback(self.slider_1, "value", self, "value", ["change"])

    # @render_effect
    # def render(self):
    #     self.slider_1.value = self.value
    #     self.progress_circle_1.value = self.value

    # def slider_1_change(self, handle, **event_args):
    #     """This method is called when the slider has finished sliding"""
    #     self.value = self.slider_1.value

    