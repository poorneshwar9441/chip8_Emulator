from Registers import Register
from memory import Ram
from helpers import First_N_Bits as F_N
from helpers import Merge_Instructions,BitVector
import random
import pygame as pg

class Processor(object):
    
    def __init__(self,screen,file):
        self.VRegistors = []
        self.Ram = Ram()
        self.Ram.load(file)
        self.pc = 0x200
        self.display = screen
       
        self.Vf_flag = Register()
        for i in range(16):
            self.VRegistors.append(Register())
            
        self.Dt_reg = Register() # Delay Timer  
        self.St_reg = Register() #Sound Timer 
        self.Sp = 0
        self.stack = []
        self.I = Register()
        for i in range(17):
            self.stack.append(0)
            
        self.Disp_values = []
        x = []
        
        for i in range(32):
            x = []
            for j in range(64):
                x.append(0)
                
            self.Disp_values.append(x)
                
    
        
    
            
    
        
    def fetch(self):
        """
        Each instruction is 2bytes long
        """
        
        if(self.pc > 0xFFF):
            return -1
        
        instruction1 = self.Ram.get_loc(self.pc)
        instruction2 = self.Ram.get_loc(self.pc+1)
        
        self.pc += 2
        
        self.decode_and_Execute(instruction1,instruction2)
        
        
    def decode_and_Execute(self,instruction1,instruction2):
        
        
        """
        A->10
        B->11
        c->12
        D->13
        E->14
        F->15
        
        """
        
        first_op = F_N(instruction1,0,4,8)
        second_op = F_N(instruction1,4,8,8)
        Third_op = F_N(instruction2,0,4,8)
        Fourth_op = F_N(instruction2,4,8,8)
        
        Merged_Ins = Merge_Instructions(instruction1,instruction2)
        
        if(first_op == 0):
            if(second_op == 0):
                if((Third_op == 14) and (Fourth_op == 0)):
                    self.display.screen.fill((0,0,0))
                    print("Ins1")
                    
                
                elif((Third_op == 14) and (Fourth_op == 14)):
                    #return from a subroutine
                    print("Ins2")
                    if(self.Sp == 0):
                        print("stack overflow Program Terminated")
                        return 0
                    self.pc = self.stack[self.Sp]
                    self.Sp -= 1
                    
            
        elif(first_op == 1):
            #JUMP addr
            
            addr = F_N(int(Merged_Ins),4,16,16)
            self.pc = addr
            print("Ins3",hex(addr))
            
            
            
        elif(first_op == 2):
            #call addr
            print("Ins4")
            self.Sp += 1
            self.stack[self.Sp] = self.pc
            self.pc = F_N(int(Merged_Ins),4,16,16)
            
        elif(first_op == 3):
            print("Ins5")
            if(self.VRegistors[second_op].value == instruction2):
                self.pc += 2
                
        elif(first_op == 4):
            print("Ins6")
            if(self.VRegistors[second_op].value != instruction2):
                self.pc += 2
                
                
        elif(first_op == 5):
            print("Ins7")
            if(self.VRegistors[second_op].value == self.VRegistors[Third_op].value):
                self.pc += 2
                
        
        elif(first_op == 6):
            print("Ins8")
            self.VRegistors[second_op].value = instruction2
            
        elif(first_op == 7):
            print("Ins9")
            self.VRegistors[second_op].value += instruction2
            
            
        elif(first_op == 8):
            if(Fourth_op == 0):
                print("Ins10")
                self.VRegistors[second_op].value = self.VRegistors[Third_op].value
                
            elif(Fourth_op == 1):
                print("Ins11")
                self.VRegistors[second_op].value = self.VRegistors[second_op].value | self.VRegistors[Third_op].value
                
                
            elif(Fourth_op == 2):
                print("Ins12")
                self.VRegistors[second_op].value = self.VRegistors[second_op].value & self.VRegistors[Third_op].value
                
                
            elif(Fourth_op == 3):
                print("Ins13")
                self.VRegistors[second_op].value = self.VRegistors[second_op].value ^ self.VRegistors[Third_op].value
                
                
            elif(Fourth_op == 4):
                print("Ins14")
                self.VRegistors[second_op].value = self.VRegistors[second_op].value + self.VRegistors[Third_op].value
                
                
                if(self.VRegistors[second_op].value > 255):
                    self.VRegistors[second_op].value = self.VRegistors[second_op].value-256
                    self.Vf_flag.value = 1
                    
                else:
                    self.Vf_flag.value = 0
                    
                    
            elif(Fourth_op == 5):
                print("Ins15")
                
                
                if(self.VRegistors[second_op].value > self.VRegistors[Third_op].value):
                    self.Vf_flag.value = 1
                else:
                    self.Vf_flag.value = 0
                    
                self.VRegistors[second_op].value = self.VRegistors[second_op].value - self.VRegistors[Third_op].value
                if(self.VRegistors[second_op].value < 0):
                    self.VRegistors[second_op].value += 256
                
            elif(Fourth_op == 6):
                print("Ins16")
                bits_vx = BitVector(intVal = self.VRegistors[second_op].value,size = 8)
                if(bits_vx[7] == 1):
                    self.Vf_flag.value = 1
                else:
                    self.Vf_flag.value = 0
                    
                self.VRegistors[second_op].value = self.VRegistors[second_op].value/2
                
            elif(Fourth_op == 7):
                print("Ins17")
                
                
                if(self.VRegistors[second_op].value > self.VRegistors[Third_op].value):
                    self.Vf_flag.value = 0
                else:
                    self.Vf_flag.value = 1
                    
                self.VRegistors[second_op].value = self.VRegistors[second_op].value - self.VRegistors[Third_op].value
                if(self.VRegistors[second_op].value < 0):
                    self.VRegistors[second_op].value += 256
                    
                    
            elif(Fourth_op == 14):
                print("Ins18")
                bits_vx = BitVector(intVal = self.VRegistors[second_op].value,size = 8)
                if(bits_vx[0] == 1):
                    self.Vf_flag.value = 1
                else:
                    self.Vf_flag.value = 0
                    
                self.VRegistors[second_op].value = self.VRegistors[second_op].value*2
                
                
        elif(first_op == 9):
            print("Ins19")
            if(self.VRegistors[second_op].value != self.VRegistors[Third_op].value):
                self.pc += 2
                
                
        elif(first_op == 0xA):
            print("Ins20")
            self.I.value = F_N(int(Merged_Ins),4,16,16)
            
        elif(first_op == 0xB):
            print("Ins21")
            self.pc = F_N(int(Merged_Ins),4,16,16) + self.VRegistors[0].value
            
        elif(first_op == 0xC):
            print("Ins22")
            self.VRegistors[second_op].value = random.randint(0,255) & instruction2
            
        elif(first_op == 0xD):
            #Draw Instuction come again
            print("Ins23")
            
            self.Draw_Instruction(second_op,Third_op,Fourth_op)
            
            
        elif(first_op == 0xE):
            #key Board Handler
            pass
        
        elif(first_op == 0xF):
            
            if(instruction2 == 7):
                print("Ins24")
                self.VRegistors[second_op].value = self.Dt_reg.value
                
            if(instruction2 == 0x0A):
                #wait for a Key press
                pass
            
            if(instruction2 == 0x15):
                print("Ins25")
                self.Dt_reg.value = self.VRegistors[second_op].value
                
            if(instruction2 == 0x18):
                print("Ins26")
                self.St_reg.value = self.VRegistors[second_op].value
                
            if(instruction2 == 0x1E):
                print("Ins27")
                self.I.value = self.I.value + self.VRegistors[second_op].value
                
                
            if(instruction2 == 0x29):
                print("Ins28")
                self.I.value = self.VRegistors[second_op].value*5
                
            if(instruction2 == 0x33):
                print("Ins29")
                vx = self.VRegistors[second_op].value
                vx_100s = int(vx/100)
                vx_ones = vx%10
                vx = vx/10
                vx_10s = vx%10
                
                self.Ram.set_loc(self.I.value,vx_100s)
                self.Ram.set_loc(self.I.value+1,vx_10s)
                self.Ram.set_loc(self.I.value+2,vx_ones)
                
                
            if(instruction2 == 0x55):
                print("Ins30")
                loc = self.I.value
                for i in range(second_op+1):
                    self.Ram.set_loc(loc,self.VRegistors[i].value)
                    loc += 1
                    
                    
            if(instruction2 == 0x65):
                print("Ins31")
                loc = self.I.value
                for i in range(second_op+1):
                    self.VRegistors[i].value = self.Ram.get_loc(loc)
                    loc += 1
                    
    def Draw_Instruction(self,second_op,Third_op,Fourth_op):
        x_cor = self.VRegistors[second_op].value%64
        y_cor = self.VRegistors[Third_op].value%32
        new_x_cor = x_cor
        n = Fourth_op
        loc = int(self.I.value)
        
        
        self.Vf_flag.value = 0
        
        
        if(x_cor < 0):
            x_cor += 64
        if(y_cor < 0):
            y_cor += 32
            
        
       
        
        for i in range(n):
            sprite_data = BitVector(intVal = self.Ram.get_loc(loc),size = 8)
            x_cor = new_x_cor
            
        
            for j in range(8):
                #if(x_cor > 63):
                  # x_cor = x_cor - 64
                #if(y_cor > 31):
                    #y_cor = y_cor - 32
                    
                if(x_cor > 63 or y_cor > 31):
                    continue
                    
                
                if(sprite_data[j] == 1):
                    if(self.Disp_values[y_cor][x_cor] == 1):
                        self.Disp_values[y_cor][x_cor] = 0
                        self.Vf_flag.value = 1
                        
                        
                    else:
                        self.Disp_values[y_cor][x_cor] = 1
                        
                        
                x_cor += 1
                
            y_cor += 1
            loc += 1
            
        
    
    def Execute(self):
        pass
        

