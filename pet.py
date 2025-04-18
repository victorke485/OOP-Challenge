class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    def eat(self):
        # TODO
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} is eating...")

    def sleep(self):
        # TODO
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} is sleeping...")

    def play(self):
        # TODO
        if self.energy <= 0:
            print(f"{self.name} is too tired to play.")
            return
        self.energy = max(0, self.energy - 2)
        self.happiness = min(10, self.happiness + 2)
        self.hunger = min(10, self.hunger + 1)
        print(f"{self.name} is playing...")

    def train(self, trick):
        # TODO
        self.tricks.append(trick)
        print(f"{self.name} learned a new trick: {trick}!")

    def show_tricks(self):
        # TODO
        if not self.tricks:
            print(f"{self.name} doesn't know any tricks yet.")
        else:
            print(f"{self.name} knows these tricks: {', '.join(self.tricks)}")

    def get_status(self):
        # TODO
        print(f"\n{self.name}'s current status:")
        print(f"Hunger: {self.hunger}")
        print(f"Energy: {self.energy}")
        print(f"Happiness: {self.happiness}")
        print(f"Tricks: {self.tricks if self.tricks else 'None'}\n")
