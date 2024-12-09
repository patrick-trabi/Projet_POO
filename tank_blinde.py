from unit import Unit

class TankBlinde(Unit):
    
    def __init__(self, x, y, health=200, attack_power=25, team="player"):
        super().__init__(x, y, health, attack_power, team)
        self.defense = 50
        self.speed = 1
        self.skills = ["Heavy Slash", "Shield Block", "Taunt"]

    def use_skill(self, skill, targets, grid):
        if skill == "Heavy Slash":
            for target in targets:
                if abs(self.x - target.x) <= 1 and abs(self.y - target.y) <= 1:
                    target.health -= 30
        elif skill == "Shield Block":
            self.defense += 20
        elif skill == "Taunt":
            # Logique pour forcer les ennemis à l'attaquer
            pass
