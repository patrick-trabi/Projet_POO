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
    Hérite de la classe Unit et ajoute des caractéristiques spécifiques.
    """
    def __init__(self, x, y, health=100, attack_power=30, defense=20, speed=3, team="player"):
        """
        Initialise un Sorcier Ninja avec des caractéristiques spécifiques.

        Paramètres
        ----------
        x : int
            Position x de l'unité sur la grille.
        y : int
            Position y de l'unité sur la grille.
        health : int
            Points de vie de l'unité (par défaut 100).
        attack_power : int
            Puissance d'attaque de l'unité (par défaut 30).
        defense : int
            Statistique de défense de l'unité (par défaut 20).
        speed : int
            Vitesse de l'unité, définissant son déplacement (par défaut 3).
        team : str
            Équipe de l'unité ("player" par défaut).
        """
        super().__init__(x, y, health, attack_power, team)
        self.defense = defense  # Défense de l'unité
        self.speed = speed      # Vitesse de déplacement

    def take_damage(self, damage):
        """
        Réduit les points de vie en fonction des dégâts subis et de la défense.

        Paramètres
        ----------
        damage : int
            Les dégâts infligés à l'unité.
        """
        actual_damage = max(0, damage - self.defense)  # Réduction des dégâts par la défense
        self.health -= actual_damage

    def move(self, dx, dy):
        """
        Déplace le Sorcier Ninja sur la grille en respectant sa vitesse.

        Paramètres
        ----------
        dx : int
            Déplacement en x.
        dy : int
            Déplacement en y.
        """
        if abs(dx) <= self.speed and abs(dy) <= self.speed:  # Vérifie si le déplacement respecte la vitesse
            super().move(dx, dy)
        else:
            raise ValueError(f"Déplacement trop important : vitesse maximale = {self.speed}")

    def attack(self, target):
        """
        Attaque une unité cible.

        Paramètres
        ----------
        target : Unit
            L'unité cible de l'attaque.
        """
        target.take_damage(self.attack_power)

    def draw(self, screen):
        """
        Affiche le Sorcier Ninja sur l'écran.

        Paramètres
        ----------
        screen : pygame.Surface
            Surface de l'écran où dessiner l'unité.
        """
        color = (75, 0, 130)  # Couleur spécifique pour le Sorcier Ninja (indigo)
        pygame.draw.circle(screen, color, (self.x * CELL_SIZE + CELL_SIZE // 2, self.y * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 3)
        if self.team == "player":
            pygame.draw.circle(screen, (0, 255, 0), (self.x * CELL_SIZE + CELL_SIZE // 2, self.y * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 3, 2)


class Samurai(Unit):
    """
    Classe pour représenter le Samurai.
    Hérite de la classe Unit et ajoute des caractéristiques spécifiques.
    """
    def __init__(self, x, y, health=150, attack_power=40, defense=30, speed=2, team="player"):
        """
        Initialise un Samurai avec des caractéristiques spécifiques.

        Paramètres
        ----------
        x : int
            Position x de l'unité sur la grille.
        y : int
            Position y de l'unité sur la grille.
        health : int
            Points de vie de l'unité (par défaut 150).
        attack_power : int
            Puissance d'attaque de l'unité (par défaut 40).
        defense : int
            Statistique de défense de l'unité (par défaut 30).
        speed : int
            Vitesse de l'unité, définissant son déplacement (par défaut 2).
        team : str
            Équipe de l'unité ("player" par défaut).
        """
        super().__init__(x, y, health, attack_power, team)
        self.defense = defense  # Défense de l'unité
        self.speed = speed      # Vitesse de déplacement

    def take_damage(self, damage):
        """
        Réduit les points de vie en fonction des dégâts subis et de la défense.

        Paramètres
        ----------
        damage : int
            Les dégâts infligés à l'unité.
        """
        actual_damage = max(0, damage - self.defense)  # Réduction des dégâts par la défense
        self.health -= actual_damage

    def move(self, dx, dy):
        """
        Déplace le Samurai sur la grille en respectant sa vitesse.

        Paramètres
        ----------
        dx : int
            Déplacement en x.
        dy : int
            Déplacement en y.
        """
        if abs(dx) <= self.speed and abs(dy) <= self.speed:  # Vérifie si le déplacement respecte la vitesse
            super().move(dx, dy)
        else:
            raise ValueError(f"Déplacement trop important : vitesse maximale = {self.speed}")

    def attack(self, target):
        """
        Attaque une unité cible.

        Paramètres
        ----------
        target : Unit
            L'unité cible de l'attaque.
        """
        target.take_damage(self.attack_power)

    def draw(self, screen):
        """
        Affiche le Samurai sur l'écran.

        Paramètres
        ----------
        screen : pygame.Surface
            Surface de l'écran où dessiner l'unité.
        """
        color = (255, 0, 0)  # Rouge pour le Samurai
        pygame.draw.circle(screen, color, (self.x * CELL_SIZE + CELL_SIZE // 2, self.y * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 3)
        if self.team == "player":
            pygame.draw.circle(screen, (0, 255, 0), (self.x * CELL_SIZE + CELL_SIZE // 2, self.y * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 3, 2)

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
    def __init__(self, x, y, health=90, attack_power=50, defense=15, speed=4, team="player"):
        """
        Initialise un Assassin Furtif avec des caractéristiques spécifiques.

        Paramètres
        ----------
        x : int
            Position x de l'unité sur la grille.
        y : int
            Position y de l'unité sur la grille.
        health : int
            Points de vie de l'unité (par défaut 90).
        attack_power : int
            Puissance d'attaque de l'unité (par défaut 50).
        defense : int
            Statistique de défense de l'unité (par défaut 15).
        speed : int
            Vitesse de l'unité, définissant son déplacement (par défaut 4).
        team : str
            Équipe de l'unité ("player" par défaut).
        """
        super().__init__(x, y, health, attack_power, team)
        self.defense = defense  # Défense de l'unité
        self.speed = speed      # Vitesse de déplacement

    def take_damage(self, damage):
        """
        Réduit les points de vie en fonction des dégâts subis et de la défense.

        Paramètres
        ----------
        damage : int
            Les dégâts infligés à l'unité.
        """
        actual_damage = max(0, damage - self.defense)  # Réduction des dégâts par la défense
        self.health -= actual_damage

    def move(self, dx, dy):
        """
        Déplace l'Assassin Furtif sur la grille en respectant sa vitesse.

        Paramètres
        ----------
        dx : int
            Déplacement en x.
        dy : int
            Déplacement en y.
        """
        if abs(dx) <= self.speed and abs(dy) <= self.speed:  # Vérifie si le déplacement respecte la vitesse
            super().move(dx, dy)
        else:
            raise ValueError(f"Déplacement trop important : vitesse maximale = {self.speed}")

    def attack(self, target):
        """
        Attaque une unité cible.

        Paramètres
        ----------
        target : Unit
            L'unité cible de l'attaque.
        """
        target.take_damage(self.attack_power)

    def draw(self, screen):
        """
        Affiche l'Assassin Furtif sur l'écran.

        Paramètres
        ----------
        screen : pygame.Surface
            Surface de l'écran où dessiner l'unité.
        """
        color = (0, 0, 0)  # Noir pour l'Assassin Furtif
        pygame.draw.circle(screen, color, (self.x * CELL_SIZE + CELL_SIZE // 2, self.y * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 3)
        if self.team == "player":
            pygame.draw.circle(screen, (0, 255, 0), (self.x * CELL_SIZE + CELL_SIZE // 2, self.y * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 3, 2)
