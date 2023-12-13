from ._anvil_designer import ProgressCircleTemplate
from anvil_reactive.main import render_effect, signal
import math

class ProgressCircle(ProgressCircleTemplate):
    """Inspired by: https://anvil.works/forum/t/progressbar-component-again/18656"""
    value = signal(0)

    def __init__(self, **properties):
        self.init_components(**properties)
        self.circ = circ = 2 * math.pi * float(self.dom_nodes["circle"].getAttribute("r"))

    @render_effect
    def render(self):
        progress = self.value or 0
        if progress > 100:
            return
        offset = self.circ * (1 - progress / 100);
        self.dom_nodes["circle"].setAttribute("stroke-dashoffset", offset)
        self.dom_nodes["text"].textContent = f"{progress:.0f}%"
