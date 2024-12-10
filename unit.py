import pygame
import random

# Constantes
GRID_SIZE = 8
CELL_SIZE = 60
WIDTH = GRID_SIZE * CELL_SIZE
HEIGHT = GRID_SIZE * CELL_SIZE
FPS = 30
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)


class Unit:
    """
    Classe pour représenter une unité.

    ...
    Attributs
    ---------
    x : int
        La position x de l'unité sur la grille.
    y : int
        La position y de l'unité sur la grille.
    health : int
        La santé de l'unité.
    attack_power : int
        La puissance d'attaque de l'unité.
    team : str
        L'équipe de l'unité ('player' ou 'enemy').
    is_selected : bool
        Si l'unité est sélectionnée ou non.

    Méthodes
    --------
    move(dx, dy)
        Déplace l'unité de dx, dy.
    attack(target)
        Attaque une unité cible.
    draw(screen)
        Dessine l'unité sur la grille.
    """

    def __init__(self, x, y, health, attack_power, team):
        """
        Construit une unité avec une position, une santé, une puissance d'attaque et une équipe.

        Paramètres
        ----------
        x : int
            La position x de l'unité sur la grille.
        y : int
            La position y de l'unité sur la grille.
        health : int
            La santé de l'unité.
        attack_power : int
            La puissance d'attaque de l'unité.
        team : str
            L'équipe de l'unité ('player' ou 'enemy').
        """
        self.x = x
        self.y = y
        self.health = health
        self.attack_power = attack_power
        self.team = team  # 'player' ou 'enemy'
        self.is_selected = False

    def move(self, dx, dy):
        """Déplace l'unité de dx, dy."""
        if 0 <= self.x + dx < GRID_SIZE and 0 <= self.y + dy < GRID_SIZE:
            self.x += dx
            self.y += dy

    def attack(self, target):
        """Attaque une unité cible."""
        if abs(self.x - target.x) <= 1 and abs(self.y - target.y) <= 1:
            target.health -= self.attack_power

    def draw(self, screen):
        """Affiche l'unité sur l'écran."""
        color = BLUE if self.team == 'player' else RED
        if self.is_selected:
            pygame.draw.rect(screen, GREEN, (self.x * CELL_SIZE,
                             self.y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        pygame.draw.circle(screen, color, (self.x * CELL_SIZE + CELL_SIZE //
                           2, self.y * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 3)



class Ninja:
    def __init__(self, x, y, health=20, attack_power=10, team=None):
        self.x = x
        self.y = y
        self.health = health
        self.attack_power = attack_power
        self.team = team
        #self.skills = [Fireball(), Evasion()]  # Compétences pour Ninja



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
