# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 15:42:25 2020

@author: SCE
"""


from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z=mc.player.getTilePos()
mc.setBlocks(x+10,y+15,z+10,x-10,y+40,z-10,49)
mc.setBlocks(x+2,y,z+2,x-2,y+20,z-2,7)