from unit import Unit

class AssassinFurtif(Unit):
    """
    Classe pour représenter l'Assassin Furtif.
    Hérite de la classe Unit.
    """
    def __init__(self, x, y, health=90, attack_power=50, team="player"):
        super().__init__(x, y, health, attack_power, team)
        self.defense = 15
        self.speed = 4
        self.skills = ["Shuriken Throw", "Shadow Step", "Critical Strike"]

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

        if skill == "Shuriken Throw":
            for target in targets:
                if abs(self.x - target.x) <= 3 and abs(self.y - target.y) <= 3:
                    target.health -= 40
                    print(f"{self.name} utilise Shuriken Throw sur {target.name} (HP restant : {target.health}).")

        elif skill == "Shadow Step":
            possible_positions = self.get_adjacent_positions(grid)
            if possible_positions:
                self.x, self.y = possible_positions[0]  # Téléportation sur la première case libre
                print(f"{self.name} se téléporte à la position ({self.x}, {self.y}).")
            else:
                print(f"{self.name} n'a aucune position disponible pour se téléporter.")

        elif skill == "Critical Strike":
            for target in targets:
                if abs(self.x - target.x) <= 1 and abs(self.y - target.y) <= 1:
                    target.health -= 60
                    print(f"{self.name} utilise Critical Strike sur {target.name} (HP restant : {target.health}).")

    def get_adjacent_positions(self, grid):
        """
        Retourne une liste de positions adjacentes disponibles sur la grille.
        """
        adjacent_positions = [
            (self.x + dx, self.y + dy)
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]
            if 0 <= self.x + dx < grid.size and 0 <= self.y + dy < grid.size and grid.is_empty(self.x + dx, self.y + dy)
        ]
        return adjacent_positions

    def draw(self, screen):
        """Dessine l'Assassin Furtif sur l'écran avec une couleur spécifique."""
        color = (255, 0, 0)  # Rouge pour l'Assassin Furtif
        super().draw(screen)
