import pygame
import random

# Constantes
grid_size = 8
cell_size = 60
width = grid_size * cell_size
height = grid_size * cell_size
fps = 30
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)

# Classe Unit
class Unit:
    def __init__(self, x, y, health, attack_power, team):
        self.x = x
        self.y = y
        self.health = health
        self.attack_power = attack_power
        self.team = team
        self.is_selected = False

    def move(self, dx, dy):
        if 0 <= self.x + dx < grid_size and 0 <= self.y + dy < grid_size:
            self.x += dx
            self.y += dy

    def attack(self, target):
        if abs(self.x - target.x) <= 1 and abs(self.y - target.y) <= 1:
            target.health -= self.attack_power

    def draw(self, screen):
        color = blue if self.team == 'player' else red
        pygame.draw.circle(screen, color, (self.x * cell_size + cell_size // 2, self.y * cell_size + cell_size // 2), cell_size // 3)

# Exemple de classes dérivées
class SorcierNinja(Unit):
    def __init__(self, x, y, team="player"):
        super().__init__(x, y, health=100, attack_power=30, team=team)

    def draw(self, screen):
        pygame.draw.circle(screen, (128, 0, 128), (self.x * cell_size + cell_size // 2, self.y * cell_size + cell_size // 2), cell_size // 3)

class TankBlinde(Unit):
    def __init__(self, x, y, team="player"):
        super().__init__(x, y, health=200, attack_power=25, team=team)

    def draw(self, screen):
        pygame.draw.circle(screen, (0, 0, 255), (self.x * cell_size + cell_size // 2, self.y * cell_size + cell_size // 2), cell_size // 3)

# Classe Game
class Game:
    def __init__(self, screen):
        self.screen = screen
        self.player_units = [SorcierNinja(0, 0, 'player'),
                             TankBlinde(1, 0, 'player')]
        self.enemy_units = [TankBlinde(6, 6, 'enemy'),
                            SorcierNinja(7, 6, 'enemy')]

    def is_visible(self, unit, target, vision_range=3):
        """
        Vérifie si la cible est dans le champ de vision d'une unité.
        
        unit : Unit
            L'unité qui cherche à voir.
        target : Unit
            L'unité cible.
        vision_range : int
            La portée de vision de l'unité.
        
        Retourne :
            True si la cible est dans le champ de vision, False sinon.
        """
        dx = abs(unit.x - target.x)
        dy = abs(unit.y - target.y)
        return dx <= vision_range and dy <= vision_range

    def handle_player_turn(self):
        for selected_unit in self.player_units:
            has_acted = False
            selected_unit.is_selected = True
            self.flip_display()
            while not has_acted:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                    if event.type == pygame.KEYDOWN:
                        dx, dy = 0, 0
                        if event.key == pygame.K_LEFT:
                            dx = -1
                        elif event.key == pygame.K_RIGHT:
                            dx = 1
                        elif event.key == pygame.K_UP:
                            dy = -1
                        elif event.key == pygame.K_DOWN:
                            dy = 1
                        selected_unit.move(dx, dy)
                        self.flip_display()
                        if event.key == pygame.K_SPACE:
                            for enemy in self.enemy_units:
                                if self.is_visible(selected_unit, enemy) and abs(selected_unit.x - enemy.x) <= 1 and abs(selected_unit.y - enemy.y) <= 1:
                                    selected_unit.attack(enemy)
                                    if enemy.health <= 0:
                                        self.enemy_units.remove(enemy)
                            has_acted = True
                            selected_unit.is_selected = False

    def handle_enemy_turn(self):
        for enemy in self.enemy_units:
            target = random.choice(self.player_units)
            dx = 1 if enemy.x < target.x else -1 if enemy.x > target.x else 0
            dy = 1 if enemy.y < target.y else -1 if enemy.y > target.y else 0
            enemy.move(dx, dy)
            if self.is_visible(enemy, target) and abs(enemy.x - target.x) <= 1 and abs(enemy.y - target.y) <= 1:
                enemy.attack(target)
                if target.health <= 0:
                    self.player_units.remove(target)

    def flip_display(self):
        self.screen.fill(black)
        for x in range(0, width, cell_size):
            for y in range(0, height, cell_size):
                rect = pygame.Rect(x, y, cell_size, cell_size)
                pygame.draw.rect(self.screen, white, rect, 1)
        for unit in self.player_units:
            unit.draw(self.screen)
            for enemy in self.enemy_units:
                if self.is_visible(unit, enemy):
                    enemy.draw(self.screen)
        for enemy in self.enemy_units:
            for unit in self.player_units:
                if self.is_visible(enemy, unit):
                    unit.draw(self.screen)
        pygame.display.flip()

# Fonction principale
def main():
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Jeu de stratégie")
    game = Game(screen)
    while True:
        game.handle_player_turn()
        game.handle_enemy_turn()

if __name__ == "__main__":
    main()




class Ninja(Unit):
    """Classe pour représenter un Ninja."""
    def __init__(self, x, y, team):
        self.x = x  # Position sur l'axe X
        self.y = y  # Position sur l'axe Y
        self.health = 20  # Santé du Ninja
        self.attack_power = 10  # Puissance d'attaque
        self.team = team  # Équipe du Ninja
        self.skills = [Fireball(), Evasion()]  # Compétences pour Ninja


class Samurai(Unit):
    """Classe pour représenter un Samurai."""
    def __init__(self, x, y, team):
        self.x = x  # Position sur l'axe X
        self.y = y  # Position sur l'axe Y
        self.health = 30  # Santé du Samurai
        self.attack_power = 8  # Puissance d'attaque
        self.team = team  # Équipe du Samurai
        self.skills = [Slash(), Shield()]  # Compétences pour Samurai


class Archer(Unit):
    """Classe pour représenter un Archer."""
    def __init__(self, x, y, team):
        self.x = x  # Position sur l'axe X
        self.y = y  # Position sur l'axe Y
        self.health = 15  # Santé de l'Archer
        self.attack_power = 7  # Puissance d'attaque
        self.team = team  # Équipe de l'Archer
        self.skills = [Arrows(), Evasion()]  # Compétences pour Archer