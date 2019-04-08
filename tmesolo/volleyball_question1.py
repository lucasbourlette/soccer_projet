#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 16:22:14 2019

@author: 3672216
"""

from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam
from soccersimulator import VolleySimulation, volley_show_simu

class RandomStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Random")

    def compute_strategy(self, state, id_team, id_player):
        return SoccerAction(acceleration=Vector2D.create_random(-1, 1),
                            shoot=Vector2D.create_random(-1, 1))

class Echauffement(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Echauffement")

    def compute_strategy(self, state, id_team, id_player):
        j=state.player_state(id_team,id_player).position
        b=state.ball.position
        p1=Vector2D(135,45)
        p2=Vector2D(45,45)
        if (id_team==1):
            return SoccerAction(acceleration=b-j,shoot=p1-b)
        if (id_team==2):
            return SoccerAction(acceleration=b-j,shoot=p2-b)

# Create teams
team1 = SoccerTeam(name="Team 1")
team2 = SoccerTeam(name="Team 2")

# Add players
team1.add("Player 1", Echauffement())  # Random strategy
team2.add("Player 2", Echauffement())   # Random strategy

# Create a match
simu = VolleySimulation(team1, team2)

# Simulate and display the match
volley_show_simu(simu)
