from unit import Unit

class SorcierNinja(Unit):
    """
    Classe pour représenter le Sorcier Ninja.
    Hérite de la classe Unit.
    """
    def __init__(self, x, y, health=100, attack_power=30, team="player"):
        super().__init__(x, y, health, attack_power, team)
        self.defense = 20
        self.speed = 2
        self.magic_energy = 100  # Énergie magique pour utiliser les compétences
        self.skills = ["Shadow Blast", "Dark Barrier", "Susanoo"]
        self.active_effects = []  # Pour suivre les bonus ou effets temporaires

    def use_skill(self, skill, targets, grid):
        """
        Exécute une compétence spécifique.
        - skill : Nom de la compétence.
        - targets : Liste des cibles affectées.
        - grid : Référence à la grille pour gérer les zones d'effet.
        """
        if skill not in self.skills:
            return

        if skill == "Shadow Blast" and self.magic_energy >= 20:
            for target in targets:
                if abs(self.x - target.x) <= 3 and abs(self.y - target.y) <= 3:
                    target.health -= 40  # Dégâts fixes
            self.magic_energy -= 20

        elif skill == "Dark Barrier" and self.magic_energy >= 30:
            self.defense += 30
            self.active_effects.append({"effect": "Dark Barrier", "duration": 2})
            self.magic_energy -= 30

        elif skill == "Susanoo" and self.magic_energy >= 50:
            self.defense += 50
            for target in grid.get_adjacent_units(self.x, self.y):  # Dégâts de zone
                target.health -= 50
            self.active_effects.append({"effect": "Susanoo", "duration": 2})
            self.magic_energy -= 50

    def end_turn(self):
        """Réduit la durée des effets actifs à chaque fin de tour."""
        for effect in self.active_effects:
            effect["duration"] -= 1
            if effect["duration"] == 0:
                if effect["effect"] == "Dark Barrier":
                    self.defense -= 30
                elif effect["effect"] == "Susanoo":
                    self.defense -= 50
        self.active_effects = [effect for effect in self.active_effects if effect["duration"] > 0]

    def draw(self, screen):
        """Dessine le Sorcier Ninja sur l'écran avec une couleur spécifique."""
        color = (128, 0, 128)  # Violet pour le Sorcier Ninja
        super().draw(screen)
