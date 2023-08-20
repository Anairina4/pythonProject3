from gui.game import Game
import pygame
import sys
from utility.constants import WIDTH, HEIGHT,SCREEN_COLOR

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
    pygame.display.set_caption('2048')
    screen.fill( SCREEN_COLOR )

    # OBJECTS
    game = Game(screen)

    # INIT

    # GUI initial call
    game.gui.show_start()

    # Initial tiles displayed
    for i in range(2): game.generate_tiles(True)

    # MAINLOOP
    while game.playing:

        # Update board game
        game.draw_board()

        # Menu?
        game.gui.menu.show()

        # Update scores
        game.gui.update_scores(game.score_manager.score, game.score_manager.best)

        # Events
        for event in pygame.event.get():

            # QUIT
            if event.type == pygame.QUIT:
                sys.exit()

            # KEYDOWN
            if event.type == pygame.KEYDOWN:

                # UP
                if event.key == pygame.K_UP:
                    game.slide_tiles('UP')

                # DOWN
                if event.key == pygame.K_DOWN:
                    game.slide_tiles('DOWN')

                # RIGHT
                if event.key == pygame.K_RIGHT:
                    game.slide_tiles('RIGHT')

                # LEFT
                if event.key == pygame.K_LEFT:
                    game.slide_tiles('LEFT')

                # NEW TILES ?
                if game.generate:
                    game.generate_tiles()
                    game.generate = False

            # MOUSE
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if game.gui.action_listener(event):
                        game.new()

        if game.is_game_over():
            game.gui.menu.active = True

        game.score_manager.check_highscore()

        pygame.display.update()

