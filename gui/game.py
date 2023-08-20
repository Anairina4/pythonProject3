import pygame
import numpy as np
import random
import sys
from utility.constants import *
from gui.interface import *
from gui.scoreManager import *

class Game:

    def __init__(self,screen):

        # TILES
        self.tiles = np.zeros( (ROWS, COLS) )
        # GUI
        self.gui = GUI(screen)
        # SCORES
        self.score_manager = ScoreManager()
        # LABEL FONT
        self.lbl_font = pygame.font.SysFont('verdana', 30, bold=True)
        # VARS
        self.generate = False
        self.playing = True

    def draw_board(self):
        rShift, cShift = GAP, GAP
        for row in range(ROWS):
            for col in range(COLS):
                tile_num = int(self.tiles[row][col])

                # TILE
                tile_color = TILES_COLORS[tile_num]
                pygame.draw.rect(self.screen, tile_color, (XSHIFT + cShift + col * TILE_SIZE, YSHIFT3 + rShift + row * TILE_SIZE, TILE_SIZE, TILE_SIZE))

                # LABEL
                tile_lbl_color = LBLS_COLORS[tile_num]
                lbl = self.lbl_font.render(str(tile_num), 0, tile_lbl_color)
                lbl_pos = (XSHIFT + cShift + col * TILE_SIZE + TILE_SIZE//2 - lbl.get_rect().width//2, YSHIFT3 + rShift + row * TILE_SIZE + TILE_SIZE//2 - lbl.get_rect().height//2)
                self.screen.blit(lbl, lbl_pos)

                cShift += GAP

            rShift += GAP
            cShift = GAP

    def generate_tiles(self, first=False):
        empty_tiles = []

        for row in range(ROWS):
            for col in range(COLS):
                if self.tiles[row][col] == 0: empty_tiles.append( (row, col) )

        idx = random.randrange(0, len(empty_tiles))
        row, col = empty_tiles[idx]
        rnd = random.randint(1, 10)
        tile_value = 2
        if not first and rnd > 7: tile_value = 4
        self.tiles[row][col] = tile_value

    def __move_and_merge(self, direction, row, col):
        dx, dy = 0, 0
        if direction == 'UP': dy = -1
        elif direction == 'DOWN': dy = 1
        elif direction == 'RIGHT': dx = 1
        elif direction == 'LEFT': dx = -1

        try:
            #MOVE
            if self.tiles[row + dy][col + dx] == 0:
                value = self.tiles[row][col]
                self.tiles[row][col] = 0
                self.tiles[row + dy][col + dx] = value
                self.generate = True
                self.__move_and_merge(direction, row + dy, col + dx)
            elif self.tiles[row][col] == self.tiles[row + dy][col + dx]:
                self.tiles[row][col] = 0
                self.tiles[row + dy][col + dx] *= 2
                self.score_manager.score += int(self.tiles[row + dy][col + dx])
                self.generate = True
        except IndexError: return

    def slide_tiles(self, direction):
        # UP
        if direction == 'UP':
            for row in range(1, ROWS):
                for col in range(COLS):
                    if self.tiles[row][col] != 0: self.__move_and_merge(direction, row, col)

        # DOWN
        if direction == 'DOWN':
            for row in range(ROWS-2, -1, -1):
                for col in range(COLS):
                    if self.tiles[row][col] != 0: self.__move_and_merge(direction, row, col)

        # RIIGHT
        if direction == 'RIGHT':
            for row in range(ROWS):
                for col in range(COLS-2, -1, -1):
                    if self.tiles[row][col] != 0: self.__move_and_merge(direction, row, col)

        # LEFT
        if direction == 'LEFT':
            for row in range(ROWS):
                for col in range(1, COLS):
                    if self.tiles[row][col] != 0: self.__move_and_merge(direction, row, col)

    def __full_board(self):
        for row in range(ROWS):
            for col in range(COLS):
                if self.tiles[row][col] == 0: return False
        return True

    def __no_more_moves(self):
        # UP
        for row in range(1, ROWS):
            for col in range(COLS):
                if self.tiles[row][col] == self.tiles[row-1][col]: return False

        # DOWN
        for row in range(ROWS-2, -1, -1):
            for col in range(COLS):
                if self.tiles[row][col] == self.tiles[row+1][col]: return False

        # RIIGHT
        for row in range(ROWS):
            for col in range(COLS-2, -1, -1):
                if self.tiles[row][col] == self.tiles[row][col+1]: return False

        # LEFT
        for row in range(ROWS):
            for col in range(1, COLS):
                if self.tiles[row][col] == self.tiles[row][col-1]: return False

        return True

    def is_game_over(self):
        if self.__full_board():
            return self.__no_more_moves()

    def new(self):
        self.tiles = np.zeros( (ROWS, COLS) )
        self.score_manager.reset_score()
        self.generate_tiles()





