from turtle import Screen
from processor import Processor
from display import Display
import pygame as pg
import sys

pg.init()
d = Display()
p = Processor(d,sys.argv[1])
clock = pg.time.Clock()


def main_loop():
    while True:
        d.screen.fill((0,0,0))

        for e in pg.event.get():
            if(e.type == pg.QUIT):
                pg.quit()
                sys.exit()
                
        p.fetch()
        
        for y in range(len(p.Disp_values)):
            for x in range(len(p.Disp_values[0])):
                if(p.Disp_values[y][x] == 1):
                    pg.draw.rect(d.screen,(0,255,0),pg.Rect(x*d.scale,y*d.scale,d.scale, d.scale))
                    
                    
        if(p.Dt_reg.value > 0):
            p.Dt_reg.value -= 1
        
        if(p.St_reg.value > 0):
            p.St_reg.value -= 1
            
        
        
        pg.display.update()
        
        
            
        
        
if __name__ == "__main__":
    main_loop()