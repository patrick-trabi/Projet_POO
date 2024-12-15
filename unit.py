import pygame
import random
from skill import Fireball, Shield, Arrows, Evasion, Slash

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
    skills : list
        Liste des compétences de l'unité.

    Méthodes
    --------
    move(dx, dy)
        Déplace l'unité de dx, dy.
    attack(target)
        Attaque une unité cible.
    use_skill(skill, target)
        Utilise une compétence sur une cible.
    draw(screen)
        Dessine l'unité sur la grille.
    """

    def __init__(self, x, y, health, attack_power, team, speed):
        """
        Construit une unité avec une position, une santé, une puissance d'attaque, une équipe et une vitesse.

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
        speed : int
            La portée de déplacement de l'unité.
        """
        self.x = x
        self.y = y
        self.health = health
        self.attack_power = attack_power
        self.team = team  # 'player' ou 'enemy'
        self.speed = speed
        self.is_selected = False
        self.skills = []

    def move(self, dx, dy):
        """Déplace l'unité de dx, dy."""
        if abs(dx) + abs(dy) <= self.speed and 0 <= self.x + dx < GRID_SIZE and 0 <= self.y + dy < GRID_SIZE:
            self.x += dx
            self.y += dy
        else:
            raise ValueError("Déplacement invalide : dépasse la portée ou hors de la grille.")

    def attack(self, target):
        """Attaque une unité cible."""
        if abs(self.x - target.x) <= 1 and abs(self.y - target.y) <= 1:
            target.health -= self.attack_power

    def use_skill(self, skill, target):
        """Utilise une compétence sur une cible."""
        if skill in self.skills:
            skill.use(self, target)
        else:
            print(f"{self.__class__.__name__} ne possède pas la compétence {skill.name}.")

    def draw(self, screen):
        """Affiche l'unité sur l'écran."""
        color = BLUE if self.team == 'player' else RED
        if self.is_selected:
            pygame.draw.rect(screen, GREEN, (self.x * CELL_SIZE, self.y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        pygame.draw.circle(screen, color, (self.x * CELL_SIZE + CELL_SIZE // 2, self.y * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 3)

class Ninja(Unit):
    def __init__(self, x, y, team):
        super().__init__(x, y, health=20, attack_power=10, team=team, speed=4)
        self.skills = [Evasion(), Arrows()]

class SorcierNinja(Unit):
    """
    Classe pour représenter le Sorcier Ninja.
    Hérite de la classe Unit et ajoute des caractéristiques spécifiques.
    """
    def __init__(self, x, y, health=100, attack_power=30, defense=20, speed=3, team="player"):
        """
        Initialise un Sorcier Ninja avec des caractéristiques spécifiques.
        """
        super().__init__(x, y, health, attack_power, team, speed)
        self.defense = defense  # Défense de l'unité
        self.skills = [Fireball(), Shield()]

    def take_damage(self, damage):
        """Réduit les points de vie en fonction des dégâts subis et de la défense."""
        actual_damage = max(0, damage - self.defense)  # Réduction des dégâts par la défense
        self.health -= actual_damage

    def draw(self, screen):
        """Affiche le Sorcier Ninja sur l'écran."""
        color = (75, 0, 130)  # Couleur spécifique pour le Sorcier Ninja (indigo)
        pygame.draw.circle(screen, color, (self.x * CELL_SIZE + CELL_SIZE // 2, self.y * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 3)
        if self.team == "player":
            pygame.draw.circle(screen, (0, 255, 0), (self.x * CELL_SIZE + CELL_SIZE // 2, self.y * CELL_SIZE // 2), CELL_SIZE // 3, 2)

class Samurai(Unit):
    """
    Classe pour représenter le Samurai.
    Hérite de la classe Unit et ajoute des caractéristiques spécifiques.
    """
    def __init__(self, x, y, health=150, attack_power=40, defense=30, speed=2, team="player"):
        """
        Initialise un Samurai avec des caractéristiques spécifiques.
        """
        super().__init__(x, y, health, attack_power, team, speed)
        self.defense = defense
        self.skills = [Slash(), Shield()]

    def take_damage(self, damage):
        """Réduit les points de vie en fonction des dégâts subis et de la défense."""
        actual_damage = max(0, damage - self.defense)  # Réduction des dégâts par la défense
        self.health -= actual_damage

        
    def draw(self, screen):
        """Affiche le Samurai sur l'écran."""
        color = (255, 0, 0)  # Rouge pour le Samurai
        pygame.draw.circle(screen, color, (self.x * CELL_SIZE + CELL_SIZE // 2, self.y * CELL_SIZE // 2), CELL_SIZE // 3)
        if self.team == "player":
            pygame.draw.circle(screen, (0, 255, 0), (self.x * CELL_SIZE + CELL_SIZE // 2, self.y * CELL_SIZE // 2), CELL_SIZE // 3, 2)

class AssassinFurtif(Unit):
    """
    Classe pour représenter l'Assassin Furtif.
    Hérite de la classe Unit.
    """
    def __init__(self, x, y, health=90, attack_power=50, defense=15, speed=4, team="player"):
        """
        Initialise un Assassin Furtif avec des caractéristiques spécifiques.
        """
        super().__init__(x, y, health, attack_power, team, speed)
        self.defense = defense
        self.skills = [Slash(), Evasion()]

    def take_damage(self, damage):
        """Réduit les points de vie en fonction des dégâts subis et de la défense."""
        actual_damage = max(0, damage - self.defense)  # Réduction des dégâts par la défense
        self.health -= actual_damage

    def draw(self, screen):
        """Affiche l'Assassin Furtif sur l'écran."""
        color = (0, 0, 0)  # Noir pour l'Assassin Furtif
        pygame.draw.circle(screen, color, (self.x * CELL_SIZE + CELL_SIZE // 2, self.y * CELL_SIZE // 2), CELL_SIZE // 3)
        if self.team == "player":
            pygame.draw.circle(screen, (0, 255, 0), (self.x * CELL_SIZE + CELL_SIZE // 2, self.y * CELL_SIZE // 2), CELL_SIZE // 3, 2)


