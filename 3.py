# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 13:55:52 2020

@author: SCE
"""


from mcpi.minecraft import Minecraft

mc=Minecraft.create()

mc.postToChat("I am watching you.")

while True:
    x,y,z=mc.player.getTilePos()
    mc.postToChat("You are located on X:"+str(x)+",Y"+str(y)+",Z"+str(z))