from unit import Unit

class NinjaElementaire(Unit):
    def __init__(self, x, y, health=110, attack_power=35, team="player"):
        super().__init__(x, y, health, attack_power, team)
        self.defense = 20
        self.speed = 3
        self.skills = ["Flame Burst", "Burning Field", "Fireball"]

    def use_skill(self, skill, targets, grid):
        if skill == "Flame Burst":
            for target in targets:
                target.health -= 45
        elif skill == "Burning Field":
            # Logique pour créer une zone persistante
            pass
        elif skill == "Fireball":
            for target in targets:
                target.health -= 50
