import pygame
from utility.constants import *

class Menu:

    def __init__(self,screen):

        # TRANSPARENT SCREEN
        self.transparent_screen = pygame.Surface( (BOARD_WIDTH, BOARD_HEIGHT) )
        self.transparent_screen.set_alpha( TRANSPARENT_ALPHA )
        self.transparent_screen.fill( WHITE )

        # GAME OVER
        self.go_font = pygame.font.SysFont('verdana', 30, True)
        self.go_lbl = self.go_font.render('Game over!', 1, GAMEOVER_LBL_COLOR)
        self.go_pos = (XSHIFT + BOARD_WIDTH//2 - self.go_lbl.get_rect().width//2, YSHIFT3 + BOARD_HEIGHT//2 - self.go_lbl.get_rect().height//2 - 35)

        # TRY AGAIN
        self.tryagain_btn = pygame.image.load('../images/tryagain_btn.png')
        self.tryagain_btn = pygame.transform.scale(self.tryagain_btn, (115, 40))
        self.tryagain_btn_pos = (XSHIFT + BOARD_WIDTH//2 - self.tryagain_btn.get_width()//2, YSHIFT3 + BOARD_HEIGHT//2 - self.tryagain_btn.get_height()//2 + 35)
        self.tryagain_btn_rect = self.tryagain_btn.get_rect(topleft=self.tryagain_btn_pos)

        # VARS
        self.active = False

    def show(self):
        if self.active:
            # TRANSPARENT SCREEN
            self.screen.blit(self.transparent_screen, (XSHIFT, YSHIFT3))

            # GAME OVER LBL
            self.screen.blit(self.go_lbl, self.go_pos)

            # TRY AGAIN BTN
            self.screen.blit(self.tryagain_btn, self.tryagain_btn_pos)

    def hide(self, bg):
        self.active = False

        pygame.draw.rect(self.screen, BOARD_COLOR, bg)
