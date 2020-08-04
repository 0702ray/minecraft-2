# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 15:42:25 2020

@author: SCE
"""


from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z=mc.player.getTilePos()
try:
    block=int(input("What block do you want put?"))
    mc.setBlock(x,y,z,block)
except:
    mc.postToChat("Olny can say int")    