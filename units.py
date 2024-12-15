import pygame
from skills import Fireball, Shield, Arrows, Evasion, Slash

CELL_SIZE = 40

class Unit:
    def __init__(self, x, y, health, attack_power, team, image_path):
        self.x = x
        self.y = y
        self.health = health
        self.attack_power = attack_power
        self.team = team  # 'player' ou 'enemy'
        self.is_selected = False
        self.skills = []  # Liste des compétences

        # Chargement de l'image de l'unité
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (CELL_SIZE, CELL_SIZE))

    def move(self, dx, dy):
        """Déplace l'unité dans la grille."""
        if 0 <= self.x + dx < 800 // CELL_SIZE and 0 <= self.y + dy < 600 // CELL_SIZE:
            self.x += dx
            self.y += dy

    def attack(self, target):
        """Attaque une unité cible."""
        if abs(self.x - target.x) <= 1 and abs(self.y - target.y) <= 1:
            target.health -= self.attack_power

    def activate_skill(self, skill, targets, interface):
        """
        Active une compétence de l'unité.
        - skill : compétence à utiliser.
        - targets : liste d'unités ennemies (ou cibles valides).
        - interface : interface du jeu pour afficher les effets.
        """
        valid_targets = [
            enemy for enemy in targets
            if abs(self.x - enemy.x) <= skill.range and abs(self.y - enemy.y) <= skill.range
        ]
        if valid_targets:
            target = valid_targets[0]  # Prend la première cible valide
            skill.use(self, target)

            # Affiche l'effet visuel via l'interface
            interface.display_skill_effect(skill, target)

            # Si la cible est morte, retourner True (à retirer de la liste)
            return target.health <= 0
        else:
            print(f"Aucune cible valide pour {skill.name}.")
            return False

    def draw(self, screen):
        """Dessine l'unité sur la grille."""
        if self.is_selected:
            pygame.draw.circle(
                screen, (0, 255, 0),
                (self.x * CELL_SIZE + CELL_SIZE // 2, self.y * CELL_SIZE + CELL_SIZE // 2),
                CELL_SIZE // 2, 3
            )
        # Dessiner l'icône de l'unité
        screen.blit(self.image, (self.x * CELL_SIZE, self.y * CELL_SIZE))


class Ninja(Unit):
    def __init__(self, x, y, team):
        self.x = x
        self.y = y
        self.health = 20
        self.attack_power = 10
        self.team = team
        self.image_path = "ninja.jpg"
        self.skills = [Fireball(), Evasion()]


class Samurai(Unit):
    def __init__(self, x, y, team):
        self.x = x
        self.y = y
        self.health = 30
        self.attack_power = 8
        self.team = team
        self.image_path = "samurai.jpg"
        self.skills = [Slash(), Shield()]


class Archer(Unit):
    def __init__(self, x, y, team):
        self.x = x
        self.y = y
        self.health = 15
        self.attack_power = 7
        self.team = team
        self.image_path = "archer.jpg"
        self.skills = [Arrows(), Evasion()]
