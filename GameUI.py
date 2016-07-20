import pygame
import sys
from pygame.locals import *
import time
import copy

class GameUI:
    def __init__(self, width, height):
        pygame.init()
        self.SCREEN_WIDTH = width
        self.SCREEN_HEIGHT = height
        self.screen = pygame.display.set_mode((width, height), 0, 32)
        self.screen.fill((0,0,0)) # black
        pygame.display.set_caption("Tic Tac Toe")
        self.clock = pygame.time.Clock()
        self.clock.tick()
        self.__drawGrid__()
        pygame.display.update()

    def __drawGrid__(self):
        pygame.draw.line(self.screen, (255,255,255), (0, self.SCREEN_HEIGHT / 3), (self.SCREEN_WIDTH, self.SCREEN_HEIGHT/3), 2)
        pygame.draw.line(self.screen, (255,255,255), (0, self.SCREEN_HEIGHT*2 / 3), (self.SCREEN_WIDTH, self.SCREEN_HEIGHT*2/3), 2)
        pygame.draw.line(self.screen, (255,255,255), (self.SCREEN_WIDTH/3, 0), (self.SCREEN_WIDTH/3, self.SCREEN_HEIGHT), 2)
        pygame.draw.line(self.screen, (255,255,255), (self.SCREEN_WIDTH*2/3, 0), (self.SCREEN_WIDTH*2/3, self.SCREEN_HEIGHT), 2)

    def drawX(self, pos):
        pos_x1 = pos[0] * self.SCREEN_WIDTH / 3 + self.SCREEN_WIDTH / 15
        pos_y1 = pos[1] * self.SCREEN_HEIGHT / 3+ self.SCREEN_HEIGHT / 15
        pos_x2 = (pos[0]+1) * self.SCREEN_WIDTH /3 - self.SCREEN_WIDTH / 15
        pos_y2 = (pos[1]+1) * self.SCREEN_HEIGHT/3 - self.SCREEN_HEIGHT / 15
        pygame.draw.line(self.screen, (255,255,255), (pos_x1, pos_y1), (pos_x2, pos_y2), 2)
        pygame.draw.line(self.screen, (255,255,255), (pos_x1, pos_y2), (pos_x2, pos_y1), 2)
        pygame.display.update()

    def drawO(self, pos):
        pos_x = pos[0] * self.SCREEN_WIDTH/3 + self.SCREEN_WIDTH / 6
        pos_y = pos[1] * self.SCREEN_HEIGHT/3 + self.SCREEN_HEIGHT / 6
        radius = self.SCREEN_HEIGHT * 2 / 15
        pygame.draw.circle(self.screen, (255,255,255), (pos_x, pos_y), radius, 2)
        pygame.display.update()

    def GetMousePos(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                mousePos = pygame.mouse.get_pos()
                mousePos = mousePos[0] / (self.SCREEN_WIDTH/3), mousePos[1] / (self.SCREEN_HEIGHT/3)
                return mousePos
            elif event.type == pygame.QUIT:
                sys.exit()
        return None

