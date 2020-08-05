# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 15:42:25 2020

@author: SCE
"""


from mcpi.minecraft import Minecraft
import time
import random
mc=Minecraft.create()
pos=mc.player.getTilePos()
while True:
    y=pos.y+3
    x=pos.x+random.uniform(-20, 20)
    z=pos.z+random.uniform(-20, 20)
    
    mc.spawnEntity(x,y,z,5)
    time.sleep(0.1)