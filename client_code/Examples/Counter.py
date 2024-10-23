from anvil_reactive.main import reactive_class, effect

@reactive_class
class Counter:
    def __init__(self):
        self.value = 42

    def inc(self):
        self.value += 1

    def dec(self):
        self.value -= 1

    @effect
    def log(self):
        print(f"{self.value}")


counter = Counter()