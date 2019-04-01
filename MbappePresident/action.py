#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 11:16:29 2019

@author: 3672216
"""

from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam, Simulation, show_simu
from .tools import *

from soccersimulator import settings
import math


class Move(object):
    def __init__(self,MyState):
        self.MyState = MyState
        
    @property
    def cour_vers_ballon(self):
        return SoccerAction(self.MyState.ball_position - self.MyState.my_position)
    
    def deplaceVers(self, pointx, pointy):
        dep = Vector2D(pointx, pointy)
        return SoccerAction(dep - self.MyState.my_position)
    
   
    
    
    
class Shoot(object):
    def __init__(self,MyState):
        self.MyState = MyState
        
        
    @property
    def tire_vers_but(self):
        return SoccerAction(self.MyState.ball_position_futur - self.MyState.my_position, self.MyState.goal - self.MyState.ball_position_futur)
    
    @property
    def tire_vers_corner(self):
       
        return SoccerAction(self.MyState.ball_position_futur - self.MyState.my_position, self.MyState.corner - self.MyState.ball_position_futur)
    
    @property
    def petit_tire(self):
        
        v1= self.MyState.goal-self.MyState.my_position
        return v1.normalize()*1      
        
    
    def passe(self, puissance, position):
        return SoccerAction(self.MyState.ball_position.normalize*puissance - position)
        equipier = self.MyState.equipier_le_plus_proche
        return SoccerAction(self.MyState.my_position - self.MyState.ball_position, equipier - self.MyState.ball_position)