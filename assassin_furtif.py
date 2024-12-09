from unit import Unit

class AssassinFurtif(Unit):
    
    def __init__(self, x, y, health=90, attack_power=50, team="player"):
        super().__init__(x, y, health, attack_power, team)
        self.defense = 15
        self.speed = 4
        self.skills = ["Shuriken Throw", "Shadow Step", "Critical Strike"]

    def use_skill(self, skill, targets, grid):
        if skill == "Shuriken Throw":
            for target in targets:
                if abs(self.x - target.x) <= 3 and abs(self.y - target.y) <= 3:
                    target.health -= 40
        elif skill == "Shadow Step":
            # Logique pour téléportation
            pass
        elif skill == "Critical Strike":
            for target in targets:
                if abs(self.x - target.x) <= 1 and abs(self.y - target.y) <= 1:
                    target.health -= 60
