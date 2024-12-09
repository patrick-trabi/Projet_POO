from unit import Unit

class EpeistePolyvalent(Unit):
    """
    Classe pour représenter l'Épéiste Polyvalent.
    Hérite de la classe Unit.
    """
    def __init__(self, x, y, health=150, attack_power=40, team="player"):
        super().__init__(x, y, health, attack_power, team)
        self.defense = 30
        self.speed = 2
        self.skills = ["Blade Dash", "Defensive Stance", "Quick Strike"]

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

        if skill == "Blade Dash":
            for target in grid.get_line_units(self.x, self.y):  # Cibles alignées
                target.health -= 35
                print(f"{self.name} utilise Blade Dash sur {target.name} (HP restant : {target.health}).")

        elif skill == "Defensive Stance":
            self.defense += 10
            print(f"{self.name} adopte une posture défensive. Défense augmentée à {self.defense}.")

        elif skill == "Quick Strike":
            for target in targets:
                if abs(self.x - target.x) <= 1 and abs(self.y - target.y) <= 1:
                    target.health -= 20
                    print(f"{self.name} utilise Quick Strike sur {target.name} (HP restant : {target.health}).")

    def draw(self, screen):
        """Dessine l'Épéiste Polyvalent sur l'écran avec une couleur spécifique."""
        color = (255, 255, 0)  # Jaune pour l'Épéiste Polyvalent
        super().draw(screen)
