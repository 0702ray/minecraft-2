# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 15:42:25 2020

@author: SCE
"""


from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z=mc.player.getTilePos()
mc.setSign(x,y,z,68,0,"I love","cellphone","and I love","computer,too")