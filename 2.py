# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 10:55:25 2020

@author: SCE
"""


from mcpi.minecraft import Minecraft

mc = Minecraft.create()

x=100
y=500
z=100

mc.player.setTilePos(x,y,z)