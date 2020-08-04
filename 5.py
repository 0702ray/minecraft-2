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

mc.setBlocks(x+20,y-20,z+20,x-20,y,z-20,22)
time.sleep(0.5)
