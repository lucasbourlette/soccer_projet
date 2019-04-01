# -*- coding: utf-8 -*-
"""
Éditeur de Spyder
Ceci est un script temporaire.
"""

from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam, Simulation, show_simu

from soccersimulator import settings
from . import tools, action
import math
import random

class Defense2Strategy(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Defense")

    def compute_strategy(self, state, id_team, id_player):
        s = tools.MyState(state,id_team,id_player)
        m = action.Move(s)
        t = action.Shoot(s)
        defenseur = Vector2D((id_team-1)*settings.GAME_WIDTH,settings.GAME_HEIGHT/2.)
        
        #s.deplaceVers(settings.GAME_WIDTH - 10, settings.GAME_HEIGHT/2.)
        
        if (s.ball_position.distance(defenseur)< settings.GAME_WIDTH/2):
            return t.tire_vers_but + m.cour_vers_ballon    
        if (s.position_adv.distance(defenseur) > settings.GAME_WIDTH/2.):
            if (s.id_team == 1):
                return  m.deplaceVers(30, settings.GAME_HEIGHT/2.)
            if (s.id_team == 2):
                return  m.deplaceVers(settings.GAME_WIDTH - 30, settings.GAME_HEIGHT/2.)
        
        if (s.position_adv.distance(defenseur) < settings.GAME_WIDTH/3.):
            return  t.tire_vers_corner + m.deplaceVers(30, settings.GAME_HEIGHT/2.)
              
        

    
class Fonceur2Strategy(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Fonceur")

    def compute_strategy(self, state, id_team, id_player):
        
        s = tools.MyState(state,id_team,id_player)
        m = action.Move(s)
        t = action.Shoot(s)
        a1=m.cour_vers_ballon
        a2=SoccerAction(None,t.petit_tire)
        a3=t.tire_vers_but
        
        while s.my_positionx<110:
            if(s.my_positionx<20):
                return a1+a3
            return a1+a2
        return a1+a3
    
    
class Attaquant(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Attaquant")

    def compute_strategy(self, state, id_team, id_player):
        s = tools.MyState(state,id_team,id_player)
        if s.att[2] : 
            return SoccerAction(Vector2D(settings.GAME_WIDTH*(s.defe[0]), (s.ball_position_futur.y + s.goal.y)/2 )-s.my_position, s.goal - s.my_position)
        else :
            return s.stratatt
        
#class AttaqueStrategy(Strategy):
#    def __init__(self):
#        Strategy.__init__(self, "Attaque")
#
#    def compute_strategy(self, state, id_team, id_player):
#         s = tools.MyState(state,id_team,id_player)
#         return s.passe

