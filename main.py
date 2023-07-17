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



                
        p.fetch()
        
        for y in range(len(p.Disp_values)):
            for x in range(len(p.Disp_values[0])):
                if(p.Disp_values[y][x] == 1):
                    pg.draw.rect(d.screen,(0,255,0),pg.Rect(x*d.scale,y*d.scale,d.scale, d.scale))



                    
                    
        if(p.Dt_reg.value > 0):
            p.Dt_reg.value -= 1
        
        if(p.St_reg.value > 0):
            p.St_reg.value -= 1



        for e in pg.event.get():
            if(e.type == pg.QUIT):
                pg.quit()
                sys.exit()

            if(e.type == pg.KEYDOWN):
                if(((e.key - ord('0')) >= 0) and ((e.key-ord('0')) <= 9)):
                    print(e.key - ord('0'), "pressed")
                    p.keyboard.dic[e.key - ord('0')] = True

                if(((e.key - ord('a')) >= 0) and ((e.key-ord('a')) <= 5)):
                    p.keyboard.dic[e.key - ord('a') + 10] = True


        for e in pg.event.get():
            if(e.type == pg.KEYUP):
                if(((e.key - ord('0')) >= 0) and ((e.key-ord('0')) <= 9)):
                    print(e.key - ord('0'), "un pressed")
                    p.keyboard.dic[e.key - ord('0')] = False

                if(((e.key - ord('a')) >= 0) and ((e.key-ord('a')) <= 5)):
                    p.keyboard.dic[e.key -ord('a') + 10] = False

            
        
        
        pg.display.update()
        
        
            
        
        
if __name__ == "__main__":
    main_loop()