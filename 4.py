# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 15:42:25 2020

@author: SCE
"""


from mcpi.minecraft import Minecraft
import time

mc=Minecraft.create()
time.sleep(5)

x,y,z=mc.player.getTilePos()

mc.setBlock(x+1,y,z,22,)
time.sleep(0.5)
mc.setBlock(x,y,z+1,22,)
time.sleep(0.5)
mc.setBlock(x+1,y,z+1,22,)
time.sleep(0.5)
mc.setBlock(x-1,y,z,22,)
time.sleep(0.5)
mc.setBlock(x,y,z-1,22 ,)
time.sleep(0.5)
mc.setBlock(x+1,y,z-1,22,)
time.sleep(0.5)
mc.setBlock(x-1,y,z-1,22,)
time.sleep(0.5)
mc.setBlock(x-1,y,z+1,22,)
mc.setBlock(x+2,y,z,22,)
time.sleep(0.5)
mc.setBlock(x,y,z+2,22,)
time.sleep(0.5)
mc.setBlock(x-2,y,z,22,)
time.sleep(0.5)
mc.setBlock(x,y,z-2,22,)
time.sleep(0.5)