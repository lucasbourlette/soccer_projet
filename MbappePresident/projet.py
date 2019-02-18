# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam, Simulation, show_simu

from soccersimulator import settings
from . import tools
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
        defenseur = Vector2D((id_team-1)*settings.GAME_WIDTH,settings.GAME_HEIGHT/2.)
        
        if (s.ball_position.distance(defenseur)< settings.GAME_WIDTH/5.):
            return s.entreBalletBut
            return SoccerAction(defenseur - s.my_position,Vector2D())    

            
class FonceurStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Defense")

    def compute_strategy(self, state, id_team, id_player):
        s = tools.MyState(state,id_team,id_player)
        return s.tire_vers_but
    
class Fonceur2Strategy(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Defense")

    def compute_strategy(self, state, id_team, id_player):
        s = tools.MyState(state,id_team,id_player)
        a1=s.cour_vers_ballon
        a2=SoccerAction(None,s.petit_tire)
        a3=s.tire_vers_but
        while s.my_positionx<110:
            if(s.my_positionx<30):
                return a1+a3
            return a1+a2
        return a1+a3

   
#team1 = SoccerTeam(name="Team 1")
#team2 = SoccerTeam(name="Team 2")
#
## Add players
##team1.add("Random", RandomStrategy()) 
#team2.add("manel", FonceurStrategy())  # Random strategy
#team1.add("zizou", Fonceur2Strategy())   # Static strategy
#
## Create a match
#simu = Simulation(team1, team2)
#
## Simulate and display the match
#show_simu(simu)