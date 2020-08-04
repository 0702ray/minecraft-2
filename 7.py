# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 15:42:25 2020

@author: SCE
"""


from mcpi.minecraft import Minecraft
import time
import random
mc=Minecraft.create()
time.sleep(5)

x,y,z=mc.player.getTilePos()

while True:
   color=random.randrange(16)
   mc.setBlocks(x+20,y-20,z+20,x-20,y,z-20,95,color)
   time.sleep(0.5)
