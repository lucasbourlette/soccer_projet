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

class FonceurStrategy(Strategy):
     def __init__(self):
        Strategy.__init__(self, "Fonceur")
        
    

     def compute_strategy(self, state, id_team, id_player):
        s = tools.MyState(state,id_team,id_player)
        if(id_team ==2):
            goal = Vector2D(0,settings.GAME_HEIGHT/2)
        else:
            goal = Vector2D(settings.GAME_WIDTH,settings.GAME_HEIGHT/2)
            
      
        return SoccerAction(s.ball_position-s.my_position, goal - s.ball_position)

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

            
class AttaqueStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Defense")

    def compute_strategy(self, state, id_team, id_player):
        s = tools.MyState(state,id_team,id_player)
        attaquant = Vector2D((id_team-1)*settings.GAME_WIDTH,settings.GAME_HEIGHT/2.)
        goal = goal = Vector2D((2-id_team)*settings.GAME_WIDTH,settings.GAME_HEIGHT/2.)
        
        if (s.ball_position.distance(attaquant) > settings.PLAYER_RADIUS ):
            return SoccerAction(s.ball_position-state.player_state(id_team,id_player).position)
        else if ()
# Create teams
         
team1 = SoccerTeam(name="Team 1")
team2 = SoccerTeam(name="Team 2")

# Add players
#team1.add("Random", RandomStrategy()) 
team2.add("manel", DefenseStrategy()) 
team2.add("reggey", FonceurStrategy()) 
team1.add("ramesh", DefenseStrategy()) # Random strategy
team1.add("zizou", FonceurStrategy())   # Static strategy

# Create a match
simu = Simulation(team1, team2)

# Simulate and display the match
show_simu(simu)
