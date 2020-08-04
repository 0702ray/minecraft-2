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
mc.setBlocks(x+20,y-10,z+20,x-20,y+10,z-20,57)
mc.setBlocks(x+19,y-9,z+19,x-19,y+9,z-19,0)
mc.setBlock(x,y-9,z,169)
mc.setBlock(x,y+9,z,169)
time.sleep(0.5)
