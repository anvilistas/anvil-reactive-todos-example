from ._anvil_designer import ProgressCircleTemplate
from anvil_reactive.main import render_effect, signal, computed
import math

class ProgressCircle(ProgressCircleTemplate):
    """Inspired by: https://anvil.works/forum/t/progressbar-component-again/18656"""
    value = signal(0)
    color = signal("")

    def __init__(self, **properties):
        self.init_components(**properties)
        self.circ = circ = 2 * math.pi * float(self.dom_nodes["circle"].getAttribute("r"))

    @render_effect
    def render_color(self):
        self.dom_nodes["circle"].setAttribute("stroke", self.color)
        self.dom_nodes["text"].setAttribute("fill", self.color)

    @computed
    @property
    def _progress(self):
        value = self.value or 0 # could be None
        return max(0, min(100, value))

    @render_effect
    def render_progress(self):
        print("rendering progress", self._progress)
        progress = self._progress
        offset = self.circ * (1 - progress / 100)
        self.dom_nodes["circle"].setAttribute("stroke-dashoffset", offset)
        self.dom_nodes["text"].textContent = f"{progress:.0f}%"
