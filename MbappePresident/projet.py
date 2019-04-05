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

class RandomStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Random")

    def compute_strategy(self, state, id_team, id_player):
        # id_team is 1 or 2
        # id_player starts at 0
    
        
        return SoccerAction(Vector2D(random.randint(-1,1),random.randint(-1,1)),Vector2D(random.randint(-1,1),random.randint(-1,1)))


class DefenseStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Defense")

    def compute_strategy(self, state, id_team, id_player):
        s = tools.MyState(state,id_team,id_player)
        defenseur = Vector2D((id_team-1)*settings.GAME_WIDTH,settings.GAME_HEIGHT/2.)
        goal = Vector2D((2-id_team)*settings.GAME_WIDTH,settings.GAME_HEIGHT/2.)
        if (s.ball_position.distance(defenseur)< settings.GAME_WIDTH/4.):
            return SoccerAction(s.ball_position_futur - s.my_position, goal - s.ball_position)
            return SoccerAction(defenseur - s.my_position,Vector2D())   
        
        
class Defense2Strategy(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Defense")

    def compute_strategy(self, state, id_team, id_player):
        s = tools.MyState(state,id_team,id_player)
        m = action.Move(s)
        t = action.Shoot(s)
        defenseur = Vector2D((id_team-1)*settings.GAME_WIDTH,settings.GAME_HEIGHT/2.)
        
        #s.deplaceVers(settings.GAME_WIDTH - 10, settings.GAME_HEIGHT/2.)
        
        
        
        ## modifier angle pour team 1
        if (s.ball_position.distance(defenseur)< settings.GAME_WIDTH/3.):
            if (s.my_positiony>=45):
                if (s.id_team == 1):
                    p=Vector2D(s.my_positionx,s.my_positiony,45)
                    return t.tire_vers(p,6) + m.cour_vers_ballon
                if (s.id_team == 2):
                    p=Vector2D(s.my_positionx,s.my_positiony,135)
                    return t.tire_vers(p,6) + m.cour_vers_ballon
            if (s.my_positiony<45):
                if (s.id_team == 1):
                    p=Vector2D(s.my_positionx,s.my_positiony,45)
                    return t.tire_vers(p,6) + m.cour_vers_ballon
                if (s.id_team == 2):
                    p=Vector2D(s.my_positionx,s.my_positiony,225)
                    return t.tire_vers(p,6) + m.cour_vers_ballon   
        
        
        
        
        
        # a regarder 
        
        
        if (s.position_adv.distance(defenseur) > settings.GAME_WIDTH/2.):
            if (s.id_team == 1):
                return  m.deplaceVers(30, settings.GAME_HEIGHT/2.)
            if (s.id_team == 2):
                return  m.deplaceVers(settings.GAME_WIDTH - 30, settings.GAME_HEIGHT/2.)
    
              
        
class FonceurStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Fonceur")

    def compute_strategy(self, state, id_team, id_player):
        s = tools.MyState(state,id_team,id_player)
        t = action.Shoot(s)
        return t.tire_vers_but
    
class Fonceur2Strategy(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Fonceur")

    def compute_strategy(self, state, id_team, id_player):
        
        s = tools.MyState(state,id_team,id_player)
        m = action.Move(s)
        t = action.Shoot(s)
        a1=m.cour_vers_ballon
        a2=SoccerAction(None,t.petit_tire(s.goal))
        a3=t.tire_vers_but
        
        while s.my_positionx<110:
            if(s.my_positionx<20):
                return a1+a3
            return a1+a2
        return a1+a3
    
    
    
    
    
class ailierh(Strategy):
    def __init__(self):
        Strategy.__init__(self, "ailierh")
        
        
        
        
    #rajouter la passe vers attaquant 4v4 pareil pour le ailier bas et tir 
    
    
    
    
    
    
    def compute_strategy(self, state, id_team, id_player): 
        s = tools.MyState(state,id_team,id_player)
        m = action.Move(s)
        t = action.Shoot(s)
        if s.ball_positiony<70 :
            return m.deplaceVers(s.ball_positionx, 70)
        if s.ball_positiony>=70 :
            if s.my_position.distance(s.oppleplusproche)<20:
                return t.tire_vers(s.equipier_le_plus_proche,2)
            if s.my_position.distance(s.goal)<40:
                return t.tire_vers_but
            else:
                if (s.id_team == 1):
                    p=Vector2D(120,70)
                    return m.cour_vers_ballon +SoccerAction(None,t.petit_tire(p))
                
                if (s.id_team == 2):
                    p=Vector2D(30,70)
                    return m.cour_vers_ballon +SoccerAction(None,t.petit_tire(p))
            
                
            
        
        
        
        
        
class ailierb(Strategy):
    def __init__(self):
        Strategy.__init__(self, "ailierb")
    
    def compute_strategy(self, state, id_team, id_player):
        s = tools.MyState(state,id_team,id_player)
        m = action.Move(s)
        t = action.Shoot(s)
        if s.ball_positiony>20 and s.ball_positionx<110 :
            return m.deplaceVers(s.ball_positionx+30, 20)
        if s.ball_positiony<=20 :
            if s.my_position.distance(s.oppleplusproche)<20:
                return t.tire_vers(s.equipier_le_plus_proche,2)
            if s.my_position.distance(s.goal)<40:
                return t.tire_vers_but
            else:
                if (s.id_team == 1):
                    p=Vector2D(120,20)
                    return m.cour_vers_ballon +SoccerAction(None,t.petit_tire(p))
                
                if (s.id_team == 2):
                    p=Vector2D(30,20)
                    return m.cour_vers_ballon +SoccerAction(None,t.petit_tire(p))
        
        
        
        
class Attaquant4v4(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Attaquant")
    
    def compute_strategy(self, state, id_team, id_player): 
        s = tools.MyState(state,id_team,id_player)
        m = action.Move(s)
        t = action.Shoot(s)
        if s.ball_positiony>70 or s.ball_positiony<20 :
            return m.deplaceVers(s.ball_positionx+15, 45)
        else :
            if (s.id_team == 1):
                if s.my_position.distance(s.oppleplusproche)<20:
                    return t.tire_vers(s.equipier_le_plus_proche,2)
                elif s.ball_positionx<110 :
                    p=Vector2D(110,45)
                    return m.cour_vers_ballon +SoccerAction(None,t.petit_tire(p))
                else :
                    return t.tire_vers_but
            if (s.id_team == 2):
                if s.my_position.distance(s.oppleplusproche)<20 and s.my_position.distance(s.goal)>40:
                    return t.tire_vers(s.equipier_le_plus_proche,2)
                elif s.ball_positionx>40:
                    p=Vector2D(40,45)
                    return m.cour_vers_ballon +SoccerAction(None,t.petit_tire(p))
                else :
                    return t.tire_vers_but
        
        
        
        
        
        
    
class Attaquant(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Attaquant")

    def compute_strategy(self, state, id_team, id_player):
        s = tools.MyState(state,id_team,id_player)
        if s.id_team == 1 :
            if (s.my_positionx < settings.GAME_WIDTH/4.) : 
                return SoccerAction(Vector2D(settings.GAME_WIDTH*(s.defe[0]), (s.ball_position_futur.y + s.goal.y)/2 )-s.my_position, s.goal - s.my_position)
            else :
                return s.stratatt
        if s.id_team == 2 :
            if (s.my_positionx > (3*settings.GAME_WIDTH)/4.) : 
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

