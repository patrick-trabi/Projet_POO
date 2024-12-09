from unit import Unit

class NinjaElementaire(Unit):
    """
    Classe pour représenter le Ninja Élémentaire (Feu).
    Hérite de la classe Unit.
    """
    def __init__(self, x, y, health=110, attack_power=35, team="player"):
        super().__init__(x, y, health, attack_power, team)
        self.defense = 20
        self.speed = 3
        self.skills = ["Flame Burst", "Burning Field", "Fireball"]
        self.active_effects = []  # Pour gérer les zones persistantes et autres effets

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

        if skill == "Flame Burst":
            for target in grid.get_area_units(self.x, self.y, radius=2):  # Zone circulaire de 1 case
                target.health -= 45
                print(f"{self.name} utilise Flame Burst sur {target.name} (HP restant : {target.health}).")

        elif skill == "Burning Field":
            affected_area = grid.get_area(self.x, self.y, radius=3)  # Zone persistante de 3 cases
            for cell in affected_area:
                cell.effects.append({"effect": "Burning Field", "damage": 10, "duration": 3})
            print(f"{self.name} crée un champ de feu dans une zone de 3 cases.")

        elif skill == "Fireball":
            for target in targets:
                if abs(self.x - target.x) <= 3 and abs(self.y - target.y) <= 3:
                    target.health -= 50
                    print(f"{self.name} utilise Fireball sur {target.name} (HP restant : {target.health}).")

    def end_turn(self):
        """Applique les effets persistants à la fin du tour."""
        for effect in self.active_effects:
            if effect["effect"] == "Burning Field":
                effect["duration"] -= 1
                if effect["duration"] == 0:
                    self.active_effects.remove(effect)

    def draw(self, screen):
        """Dessine le Ninja Élémentaire sur l'écran avec une couleur spécifique."""
        color = (255, 165, 0)  # Orange pour le Ninja Élémentaire
        super().draw(screen)
