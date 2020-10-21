#Multi waves
from tkinter import *
import time
import random

def lerp(v0, v1, w):
    lerp = (1 - w)*v0 + w*v1
    #print(lerp, v0, v1)
    return v0-lerp

class Wave():
    def __init__(self, wavespeed, waveheight, wavereach, waveat):
        self.wavespeed = wavespeed
        self.waveheight = waveheight
        self.wavereach = wavereach
        self.waveat = waveat


    def returnvals(self):
        return self.wavespeed, self.waveheight, self.wavereach, self.waveat
        
    

    def wave(self):
        print("start wave")
        
        self.wave()

updatespeed = 35
width = 1000
height = 300
bgcolour = "white"
numboxes = 30
wavesize = width/numboxes

root = Tk()
c = Canvas(root, width=width, height=height, bg=bgcolour)
blocks = []

extra = 0

for i in range(1, numboxes+1):
    blocks.append(c.create_rectangle((wavesize*i + extra)-wavesize, height/2,
                            (wavesize*i), height*2,
                            fill="blue", outline = "blue"))
c.pack()

waves = []

def addwaves():
    for i in range(-300, 0, 30):
        #wavespeed, waveheight, wavereach, waveat
        waves.append(Wave(random.randint(1, 10)/10, random.randint(30, 100), 60*(1/3.5), i)) #at least 30 between waves


while True:
    if len(waves) >= 10:
        #print("loop0")
        for k,n in enumerate(waves):
            #print("loop1")
            wavespeed, waveheight, wavereach, waveat = n.returnvals()
            #print(wavereach)
            for i,v in enumerate(blocks):
                #if i == 1:
                   #print("loop2")
                distance = i-waveat
                if distance >= -waveheight/3.5 and distance <= wavereach/3.5:

                    try:
                        lerpmod = 1/(distance + 1)
                    except ZeroDivisionError:
                        lerpmod = 1
                    
                    currentpos = c.coords(v)[1]

                    #if i == 1:
                        #print(currentpos, distance, lerpmod)
                        #print(currentpos)

                    if distance >= 0 and distance <= wavereach:
                        c.move(v, 0, -lerp(currentpos, height/2-waveheight, 1/wavereach))
                    else:
                        #if i == 1:
                            #print(currentpos)
                        #if distance < 0:
                            #print(distance, currentpos)
                        c.move(v, 0, -lerp(currentpos, height/2, 1/wavereach))
                #elif c.coords(v)[1] != height/2:
                    #print("Box: " + str(i) + " is not at the right height")
                    #c.move(v, 0, abs(c.coords(v)[1]-height/2))
            n.waveat += 1*wavespeed
            if waveat > numboxes + 30:
                del waves[k]
            

        
        time.sleep(updatespeed/1000)
        c.update()
            
        
    else:
        print("No waves")
        addwaves()
        #time.sleep(1)

#root.after(200, animate)


#width, height, bg, update, numboxes, wavespeedmod
#Wavemaker(1000, 300, "white", 20, 300, 0.5)
    
