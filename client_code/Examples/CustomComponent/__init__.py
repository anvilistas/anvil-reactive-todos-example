from ._anvil_designer import CustomComponentTemplate

class CustomComponent(CustomComponentTemplate):
    """See ProgressCircle Component, which uses reactvity"""
    def __init__(self, **properties):
        self.init_components(**properties)
        self.slider_1_change()

    def slider_1_change(self, **event_args):
        self.progress_circle_1.value = self.slider_1.value
