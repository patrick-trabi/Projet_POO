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

        # Effet visuel temporaire
        self.effect_color = None
        self.effect_timer = 0

        # Charger l'image de l'unité
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (CELL_SIZE, CELL_SIZE))

    def move(self, dx, dy):
        """Déplace l'unité dans la grille."""
        if 0 <= self.x + dx < 800 // CELL_SIZE and 0 <= self.y + dy < 600 // CELL_SIZE:
            self.x += dx
            self.y += dy

    def attack(self, target):
        #Attaque une unité cible
        if abs(self.x - target.x) <= 1 and abs(self.y - target.y) <= 1:
            target.health -= self.attack_power
            target.effect_color = (255, 0, 0)  # Rouge pour un effet visuel d'attaque
            target.effect_timer = 15  # Durée de l'effet en frames

    def draw(self, screen):
        #Dessine l'unité sur la grille
        if self.is_selected:
            pygame.draw.circle(
                screen, (0, 255, 0),
                (self.x * CELL_SIZE + CELL_SIZE // 2, self.y * CELL_SIZE + CELL_SIZE // 2),
                CELL_SIZE // 2, 3
            )

        # Applique un effet visuel temporaire
        if self.effect_timer > 0:
            temp_surface = self.image.copy()
            temp_surface.fill(self.effect_color, special_flags=pygame.BLEND_RGBA_MULT)
            screen.blit(temp_surface, (self.x * CELL_SIZE, self.y * CELL_SIZE))
            self.effect_timer -= 1
        else:
            screen.blit(self.image, (self.x * CELL_SIZE, self.y * CELL_SIZE))


class Ninja(Unit):
    def __init__(self, x, y, team):
        image_path = "alter_ninja.jpg" if team == 'enemy' else "ninja.jpg"
        super().__init__(x, y, health=20, attack_power=10, team=team, image_path=image_path)
        self.skills = [Fireball(), Evasion()]


class Samurai(Unit):
    def __init__(self, x, y, team):
        image_path = "alter_samurai.jpg" if team == 'enemy' else "samurai.jpg"
        super().__init__(x, y, health=30, attack_power=8, team=team, image_path=image_path)
        self.skills = [Slash(), Shield()]


class Archer(Unit):
    def __init__(self, x, y, team):
        image_path = "alter_archer.jpg" if team == 'enemy' else "archer.jpg"
        super().__init__(x, y, health=15, attack_power=7, team=team, image_path=image_path)
        self.skills = [Arrows(), Evasion()]
