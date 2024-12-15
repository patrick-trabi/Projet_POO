import pygame
import random
from units import Ninja, Samurai, Archer
from interface import Interface

# Dimensions de la fenêtre
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 40


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.interface = Interface(screen, WIDTH, HEIGHT)
        self.player_units = [
            Ninja(0, 0, 'player'),
            Samurai(1, 0, 'player'),
            Archer(2, 0, 'player')
        ]
        self.enemy_units = [
            Ninja(6, 6, 'enemy'),
            Samurai(7, 6, 'enemy'),
            Archer(5, 6, 'enemy')
        ]
        self.selected_target = None  # Pour stocker la cible sélectionnée

    def handle_player_turn(self):
        """Gère le tour des joueurs."""
        for unit in self.player_units:
            unit.is_selected = True
            self.interface.flip_display(self.player_units, self.enemy_units)
            action_done = False

            while not action_done:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()

                    if event.type == pygame.KEYDOWN:
                        # Gestion du déplacement
                        dx, dy = 0, 0
                        if event.key == pygame.K_LEFT:
                            dx = -1
                        elif event.key == pygame.K_RIGHT:
                            dx = 1
                        elif event.key == pygame.K_UP:
                            dy = -1
                        elif event.key == pygame.K_DOWN:
                            dy = 1
                        unit.move(dx, dy)
                        self.interface.flip_display(self.player_units, self.enemy_units)

                        # Gestion des compétences
                        if event.key in [pygame.K_1, pygame.K_2, pygame.K_3]:
                            skill_index = event.key - pygame.K_1  # 0 pour K_1, 1 pour K_2, etc.
                            if skill_index < len(unit.skills):
                                self.select_target_and_activate_skill(unit, unit.skills[skill_index])
                                action_done = True
                                unit.is_selected = False

                        # Terminer le tour (touche espace)
                        if event.key == pygame.K_SPACE:
                            for enemy in self.enemy_units:
                                if abs(unit.x - enemy.x) <= 1 and abs(unit.y - enemy.y) <= 1:
                                    unit.attack(enemy)
                                    if enemy.health <= 0:
                                        self.enemy_units.remove(enemy)
                            action_done = True
                            unit.is_selected = False

    def select_target_and_activate_skill(self, user, skill):
        """Permet au joueur de sélectionner une cible pour la compétence."""
        self.selected_target = None  # Réinitialiser la sélection
        targets = [enemy for enemy in self.enemy_units if abs(user.x - enemy.x) <= skill.range and abs(user.y - enemy.y) <= skill.range]

        if not targets:
            print("Aucune cible disponible.")
            return

        while self.selected_target is None:
            self.interface.highlight_targets(self.screen, targets)  # Affiche les cibles disponibles
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Sélection par clic
                    mouse_x, mouse_y = event.pos
                    grid_x, grid_y = mouse_x // CELL_SIZE, mouse_y // CELL_SIZE
                    for target in targets:
                        if target.x == grid_x and target.y == grid_y:
                            self.selected_target = target
                            break

        # Une fois la cible sélectionnée, activez la compétence
        skill.use(user, self.selected_target)
        if self.selected_target.health <= 0:
            self.enemy_units.remove(self.selected_target)
        print(f"{user.__class__.__name__} utilise {skill.name} sur {self.selected_target.__class__.__name__}.")

    def handle_enemy_turn(self):
        """IA basique pour les ennemis."""
        for enemy in self.enemy_units:
            target = random.choice(self.player_units)
            dx = 1 if enemy.x < target.x else -1 if enemy.x > target.x else 0
            dy = 1 if enemy.y < target.y else -1 if enemy.y > target.y else 0
            enemy.move(dx, dy)

            if abs(enemy.x - target.x) <= 1 and abs(enemy.y - target.y) <= 1:
                enemy.attack(target)
                if target.health <= 0:
                    self.player_units.remove(target)

    def run(self):
        """Boucle principale du jeu."""
        while True:
            self.handle_player_turn()
            self.handle_enemy_turn()


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Ninja Strategy")
    game = Game(screen)
    game.run()


if __name__ == "__main__":
    main()
