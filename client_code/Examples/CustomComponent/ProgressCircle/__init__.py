from ._anvil_designer import ProgressCircleTemplate
from anvil_reactive.main import render_effect, signal
import math

class ProgressCircle(ProgressCircleTemplate):
    value = signal(0)

    def __init__(self, **properties):
        self.init_components(**properties)

    @render_effect
    def render(self):
        progress = self.value or 0
        if progress >= 100:
            return

        circ = 2 * math.pi * 40
        offset = circ * (1 - progress / 100);
        self.dom_nodes["circle"].setAttribute("stroke-dashoffset", offset)
        self.dom_nodes["text"].textContent = f"{progress:.0f}%"
