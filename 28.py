# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 11:36:25 2020

@author: SCE
"""


from mcpi.minecraft import Minecraft
import time

mc = Minecraft.create()

while True:
    mc.executeCommand('time add 1000')
    time.sleep(0.0005)