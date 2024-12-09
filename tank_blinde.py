from unit import Unit

class TankBlinde(Unit):
    """
    Classe pour représenter le Tank Blindé.
    Hérite de la classe Unit.
    """
    def __init__(self, x, y, health=200, attack_power=25, team="player"):
        super().__init__(x, y, health, attack_power, team)
        self.defense = 50
        self.speed = 1
        self.skills = ["Heavy Slash", "Shield Block", "Taunt"]
        self.active_effects = []  # Pour gérer les effets temporaires

    def use_skill(self, skill, targets, grid):
        """
        Exécute une compétence spécifique.
        - skill : Nom de la compétence.
        - targets : Liste des cibles affectées.
        - grid : Référence à la grille pour gérer les zones d'effet.
        """
        if skill not in self.skills:
            print(f"{self.name} ne possède pas la compétence {skill}.")
            return

        if skill == "Heavy Slash":
            for target in grid.get_adjacent_units(self.x, self.y):
                target.health -= 30
                print(f"{self.name} utilise Heavy Slash sur {target.name} (HP restant : {target.health}).")

        elif skill == "Shield Block":
            self.defense += 20
            self.active_effects.append({"effect": "Shield Block", "duration": 1})
            print(f"{self.name} utilise Shield Block. Défense augmentée à {self.defense} pour 1 tour.")

        elif skill == "Taunt":
            for target in grid.get_adjacent_units(self.x, self.y):
                target.forced_target = self  # Ajoute une propriété pour forcer l'attaque
                print(f"{self.name} utilise Taunt sur {target.name}. {target.name} est forcé d'attaquer {self.name}.")

    def end_turn(self):
        """Réduit la durée des effets actifs à chaque fin de tour."""
        for effect in self.active_effects:
            effect["duration"] -= 1
            if effect["duration"] == 0:
                if effect["effect"] == "Shield Block":
                    self.defense -= 20
        self.active_effects = [effect for effect in self.active_effects if effect["duration"] > 0]

    def draw(self, screen):
        """Dessine le Tank Blindé sur l'écran avec une couleur spécifique."""
        color = (0, 0, 255)  # Bleu pour le Tank Blindé
        super().draw(screen)
