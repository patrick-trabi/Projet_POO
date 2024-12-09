from unit import Unit

class EpeistePolyvalent(Unit):
    
    def __init__(self, x, y, health=150, attack_power=40, team="player"):
        super().__init__(x, y, health, attack_power, team)
        self.defense = 30
        self.speed = 2
        self.skills = ["Blade Dash", "Defensive Stance", "Quick Strike"]

    def use_skill(self, skill, targets, grid):
        if skill == "Blade Dash":
            for target in targets:
                target.health -= 35
        elif skill == "Defensive Stance":
            self.defense += 10
        elif skill == "Quick Strike":
            for target in targets:
                target.health -= 20
