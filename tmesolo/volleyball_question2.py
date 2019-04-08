#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 17:28:15 2019

@author: 3672216
"""

from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam
from soccersimulator import VolleySimulation, volley_show_simu

class Attaque(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Attaque")

    def compute_strategy(self, state, id_team, id_player):
        
        j=state.player_state(1,id_player).position
        ja=state.player_state(2,id_player).position
        b=state.ball.position
        
        p1=Vector2D(135,45)
        p2=Vector2D(45,45)
        if (id_team==1):
            if(ja.x>135):
                if ja.y>45 :
                    p1=Vector2D(95,13)
                else:
                    p1=Vector2D(95,77)
            else:
                if ja.y>45 :
                    p1=Vector2D(175,13)
                else:
                    p1=Vector2D(175,77)
            return SoccerAction(acceleration=b-j,shoot=p1-b)
        if (id_team==2):
            if(ja.x>45):
                if ja.y>45 :
                    p1=Vector2D(5,13)
                else:
                    p1=Vector2D(5,77)
            else:
                if ja.y>45 :
                    p1=Vector2D(85,13)
                else:
                    p1=Vector2D(85,77)
            return SoccerAction(acceleration=b-ja,shoot=p2-b)    
           
        # Create teams
team1 = SoccerTeam(name="Team 1")
team2 = SoccerTeam(name="Team 2")

# Add players
team1.add("Player 1", Attaque())  # Random strategy
team2.add("Player 2", Attaque())   # Random strategy

# Create a match
simu = VolleySimulation(team1, team2)

# Simulate and display the match
volley_show_simu(simu)