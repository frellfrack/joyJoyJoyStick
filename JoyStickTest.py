#!/usr/bin/python3
import serial
import pygame
from math import pi,sin,cos
from time import sleep
class joyjoytest:


    def __init__(self):
    
        self.nodesOrg =[
        [0,-100],
        [-100,100],
        [100,100],
        [0,-100],
        [0,100]
        ]
        
        self.nodes = [
        [0,-100],
        [-100,100],
        [100,100],
        [0,-100],
        [0,100]
        ]
        
        
        self.nodeLables=[
        'Left X',
        'Left Y',
        'Left Z',
        'Right X',
        'Right Y',
        'Right Z',
        ]
        
        self.nodLen = 5
        self.shipcolour = (0,255,0)
        self.labelColour = (255,255,255)
        self.serialCom = serial.Serial('/dev/ttyUSB0',9600)

        pygame.init()
        self.width=1000
        self.height=400
        self.size = [self.width, self.height]
        self.screen = pygame.display.set_mode(self.size)
        self.centreX = self.width/2
        self.centreY = self.height/2
        
        self.t = 0
        pygame.display.set_caption("Joystick Test")
        programIcon = pygame.image.load('icon.png')
        pygame.display.set_icon(programIcon)

        done = False
        self.clock = pygame.time.Clock()
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    done=True 
            self.screen.fill((0,0,0))
            self.drawAnim()
        pygame.quit()
    def readValues(self):
        s_bytes = self.serialCom.readline()
        decoded_bytes = s_bytes.decode("utf-8").strip('\n')
        values = [float(x) for x in decoded_bytes.split()]
        values = [float(x) for x in decoded_bytes.split()]
        return values
    def drawAnim(self):   
        
        values = self.readValues()
        self.drawAxisValues(values)
        left_x=(values[0]/1700)*(self.centreX/2)+(self.centreX/2)
        left_y=-(values[1]/1700)*self.centreY+self.centreY
        left_z=values[2]
        
        
        self.rotate(left_z/2000)
        pygame.draw.lines(self.screen, (255,255,255), False, [[left_x,0],[left_x,self.height]], 1)
        pygame.draw.lines(self.screen, (255,255,255), False, [[0,left_y],[self.width,left_y]], 1)
        self.drawTriangle(left_x,left_y)


        
        right_x=(values[3]/1700)*(self.centreX/2)+(self.centreX/2)+self.centreX
        right_y=-(values[4]/1700)*self.centreY+self.centreY
        right_z=values[5]
                
        self.rotate(right_z/2000)
        pygame.draw.lines(self.screen, (255,255,255), False, [[right_x,0],[right_x,self.height]], 1)
        pygame.draw.lines(self.screen, (255,255,255), False, [[0,right_y],[self.width,right_y]], 1)
        self.drawTriangle(right_x,right_y)
        
        pygame.display.flip()
        
    def drawAxisValues(self, values):
        for i in range(0, 6, 1):
            message = "%s: %.2f" % (self.nodeLables[i],values[i])
            self.drawLabel ([5,30*i+10],message ,22)
            
    def rotate(self, theta):
        
        sinTheta = sin(theta)
        cosTheta = cos(theta)
        for i in range(0, self.nodLen, 1):
            x = self.nodesOrg[i][0]
            y = self.nodesOrg[i][1]
            self.nodes[i][0] = x * cosTheta - y * sinTheta
            self.nodes[i][1] = y * cosTheta + x * sinTheta
        
    def drawTriangle(self, cx,cy):
        cords = []        
        for i in range(0, self.nodLen-1, 1):
            x = round(cx + self.nodes[i][0]) 
            y = round(cy + self.nodes[i][1])             
            cords.append([x,y])
        pygame.draw.lines(self.screen, self.shipcolour, False, cords, 1)

    def drawLabel (self,cords,message,fontsize):
        font = pygame.font.SysFont(None, fontsize)
        text = font.render(message, True, self.labelColour)
        self.screen.blit(text,(cords[0], cords[1]))
         
        
tmp =  joyjoytest()
