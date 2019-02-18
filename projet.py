# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam, Simulation, show_simu

from soccersimulator import settings
import tools
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
        if (s.ball_position.distance(defenseur)< settings.GAME_WIDTH/5.):
            return SoccerAction(s.ball_position - s.my_position, goal - s.ball_position)
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
        return s.petit_tire
"""class joueur_attaquant(Strategy):
     def __init__(self):
        Strategy.__init__(self, "Attaquant")
        
     def compute_strategy(self, state, id_team, id_player):
        s= tools.MyState(state,id_team,id_player)
        i=s.goal.x
        if id_team==2: 
           if  s.ball_positionx > settings.GAME_WIDTH/100*70:  
                return SoccerAction((Vector2D(settings.GAME_WIDTH/100*65,settings.GAME_HEIGHT/2)-s.my_position),Vector2D())
        if id_team==1:
            if s.ball_positionx < settings.GAME_WIDTH/100*30:
                return SoccerAction((Vector2D(settings.GAME_WIDTH/100*35,settings.GAME_HEIGHT/2)-s.my_position),Vector2D())
        if s.norme>settings.SHORT_RANGE:
           return SoccerAction((s.ball_position + s.ball_vitesse*10-s.my_position).normalize()*settings.maxPlayerAcceleration,Vector2D())
        if s.norme>settings.BALL_RADIUS:
            return SoccerAction((s.ball_position-s.my_position),Vector2D())
        if (s.my_position.x<settings.GAME_WIDTH/2 and s.id_team==1)or(s.my_position.x>settings.GAME_WIDTH/2 and s.id_team==2):
           if s.eproche<settings.SHORT_RANGE:
                return SoccerAction((s.ball-s.player),(s.fproche).normalize()*2)
           return SoccerAction((s.ball-s.player),(Vector2D(i,settings.GAME_HEIGHT/2)-s.player).normalize()*2)
        else:
           return SoccerAction((s.ball-s.player),Vector2D(i,settings.GAME_HEIGHT/2)-s.player)"""
    
       
        
"""class AttStrate(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Defense")

    def compute_strategy(self, state, id_team, id_player):
         s = tools.MyState(state,id_team,id_player)
       return SoccerAction(Vector2D(GAME_WIDTH*(state.teamdef[0]), (s.balle_futur.y+s.goal.y)/2 )-state.player, state.goal-state.player)"""
   
team1 = SoccerTeam(name="Team 1")
team2 = SoccerTeam(name="Team 2")

# Add players
#team1.add("Random", RandomStrategy()) 
team2.add("manel", DefenseStrategy())  # Random strategy
team1.add("zizou", FonceurStrategy())   # Static strategy

# Create a match
simu = Simulation(team1, team2)

# Simulate and display the match
show_simu(simu)