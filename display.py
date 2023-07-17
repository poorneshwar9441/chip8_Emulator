import pygame as pg 
import sys
from processor import Processor

class Display:
    def __init__(self):
        
        self.scale = 15
        self.screen = pg.display.set_mode((64*self.scale,32*self.scale))
        self.screen.fill((0,0,0))