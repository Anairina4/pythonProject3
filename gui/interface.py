import os.path

import pygame
import sys
from utility.constants import *
from gui.menu import *

class GUI:

    def __init__(self,screen):

        # LOGO
       # self.logo = pygame.image.load('../images/logo.png')
        #self.logo = pygame.transform.scale(self.logo, (self.logo.get_width()//2, self.logo.get_height()//2))
        #self.logo_pos = (XSHIFT, YSHIFT)

        # SCORE RECT
        self.score = pygame.transform.scale(pygame.image.load(os.path.normpath("images/score.png")), (90,42))
        self.score_rect_pos = (XSHIFT2, YSHIFT)

        # BEST RECT
        self.best = pygame.transform.scale(pygame.image.load(os.path.normpath("images/best.png")), (90,42))
        self.best_rect_pos = (XSHIFT2 + self.score.get_width() + 2, YSHIFT)

        # SCORE & BEST VALUE
        self.score_font = pygame.font.SysFont('verdana', 15, bold=True)

        # MESSAGE
        self.message = pygame.image.load('../images/message.png')
        self.message = pygame.transform.scale(self.message, (self.message.get_width()//2, self.message.get_height()//2))
        self.message_pos = (XSHIFT, YSHIFT2)

        # NEW GAME
        self.newgame_btn = pygame.image.load('../images/newgame.png')
        self.newgame_btn = pygame.transform.scale(self.newgame_btn, (115, 40))
        self.newgame_btn_pos = (XSHIFT3, YSHIFT2)
        self.newgame_btn_rect = self.newgame_btn.get_rect(topleft=self.newgame_btn_pos)

        # BOARD
        self.board_rect = (XSHIFT, YSHIFT3, BOARD_WIDTH, BOARD_HEIGHT)

        # MENU
        self.menu = Menu(screen)

    def show_start(self):
        # LOGO
      #  self.screen.blit(self.logo, self.logo_pos)

        # SCORE
        self.screen.blit(self.score, self.score_rect_pos)

        # BEST
        self.screen.blit(self.best, self.best_rect_pos)

        # MESSAGE
        self.screen.blit(self.message, self.message_pos)

        # NEWGAME
        self.screen.blit(self.newgame_btn, self.newgame_btn_pos)

        # BOARD BG
        pygame.draw.rect(self.screen, BOARD_COLOR, self.board_rect)

        # AD
        #self.screen.blit(self.ad, self.ad_pos)

    def update_scores(self, score_value, best_value):
        # SCORE RECT
        self.screen.blit(self.score, self.score_rect_pos)

        # SCORE VALUE
        self.score_lbl = self.score_font.render(str(score_value), 0, WHITE)
        self.score_pos = (XSHIFT2 + self.score.get_width() // 2 - self.score_lbl.get_rect().width // 2, YSHIFT + self.score.get_height() // 2 - self.score_lbl.get_rect().height // 2 + 8)
        self.screen.blit(self.score_lbl, self.score_pos)

        # BEST RECT
        self.screen.blit(self.best, self.best_rect_pos)

        # BEST VALUE
        self.best_lbl = self.score_font.render(str(best_value), 0, WHITE)
        self.best_pos = (290 + self.best.get_width() // 2 - self.best_lbl.get_rect().width // 2, YSHIFT + self.best.get_height() // 2 - self.best_lbl.get_rect().height // 2 + 8)
        self.screen.blit(self.best_lbl, self.best_pos)

    def action_listener(self, event):
        # MENU
        if self.menu.active:
            if self.menu.tryagain_btn_rect.collidepoint(event.pos):
                self.menu.hide(self.board_rect)
                return True

        # TRY AGAIN BTN
        elif self.newgame_btn_rect.collidepoint(event.pos):
            return True

        return False
