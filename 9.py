# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 15:42:25 2020

@author: SCE
"""


from mcpi.minecraft import Minecraft
import time
mc=Minecraft.create()
time.sleep(5)

while True:
    x,y,z=mc.player.getTilePos()
    mc.setBlock(x,y,z,38,8)
    time.sleep(0.1)
