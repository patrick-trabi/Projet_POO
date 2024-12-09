# sorcier_ninja.py
from unit import Unit

class SorcierNinja(Unit):
    """
    Classe pour représenter le Sorcier Ninja.
    Hérite de la classe Unit.
    """
    def __init__(self, x, y, health, attack_power, team):
        super().__init__(x, y, health, attack_power, team)
        self.skills = ["Shadow Blast", "Dark Barrier", "Susanoo"]
        self.defense = 20  # Défense spécifique au Sorcier Ninja
        self.magic_energy = 100  # Énergie magique

    def use_skill(self, skill, targets, grid):
        """Exécute une compétence spécifique."""
        if skill == "Shadow Blast":
            for target in targets:
                if abs(self.x - target.x) <= 3 and abs(self.y - target.y) <= 3:  # Portée = 3
                    target.health -= 40  # Dégâts fixes
        elif skill == "Dark Barrier":
            self.defense += 30  # Bonus temporaire de défense
        elif skill == "Susanoo":
            for target in grid.get_adjacent_units(self.x, self.y):  # Zone d'effet adjacente
                target.health -= 50  # Dégâts de zone
            self.defense += 50  # Armure spirituelle
