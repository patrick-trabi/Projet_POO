from unit import Unit

class FumigateurStrategique(Unit):
    """
    Classe pour représenter le Fumigateur Stratégique.
    Hérite de la classe Unit.
    """
    def __init__(self, x, y, health=120, attack_power=30, team="player"):
        super().__init__(x, y, health, attack_power, team)
        self.defense = 25
        self.speed = 2
        self.skills = ["Smoke Bomb", "Healing Mist", "Trap Deployment"]

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

        if skill == "Smoke Bomb":
            affected_area = grid.get_area(self.x, self.y, radius=2)
            for cell in affected_area:
                cell.visibility = False
            print(f"{self.name} lance une bombe fumigène, rendant les cases autour invisibles.")

        elif skill == "Healing Mist":
            for target in targets:
                if abs(self.x - target.x) <= 2 and abs(self.y - target.y) <= 2 and target.team == self.team:
                    target.health += 30
                    print(f"{self.name} soigne {target.name}, HP augmenté à {target.health}.")

        elif skill == "Trap Deployment":
            adjacent_positions = self.get_adjacent_positions(grid)
            if adjacent_positions:
                trap_position = adjacent_positions[0]
                grid.place_trap(trap_position, damage=20, immobilize=True)
                print(f"{self.name} place un piège à la position {trap_position}.")
            else:
                print(f"{self.name} n'a aucune case adjacente disponible pour placer un piège.")

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
        """Dessine le Fumigateur Stratégique sur l'écran avec une couleur spécifique."""
        color = (0, 255, 0)  # Vert pour le Fumigateur Stratégique
        super().draw(screen)
