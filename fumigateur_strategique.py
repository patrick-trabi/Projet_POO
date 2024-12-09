from unit import Unit

class FumigateurStrategique(Unit):
    
    def __init__(self, x, y, health=120, attack_power=30, team="player"):
        super().__init__(x, y, health, attack_power, team)
        self.defense = 25
        self.speed = 2
        self.skills = ["Smoke Bomb", "Healing Mist", "Trap Deployment"]

    def use_skill(self, skill, targets, grid):
        if skill == "Smoke Bomb":
            # Logique pour réduire la visibilité des ennemis
            pass
        elif skill == "Healing Mist":
            for target in targets:
                target.health += 30
        elif skill == "Trap Deployment":
            # Logique pour poser un piège
            pass
