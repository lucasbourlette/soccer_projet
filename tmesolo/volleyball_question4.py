#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 17:58:27 2019

@author: 3672216
"""

from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam
from soccersimulator import VolleySimulation, volley_show_simu

class firstrat(Strategy):
    def __init__(self):
        Strategy.__init__(self,"1V1")

    def compute_strategy(self, state, id_team, id_player):
        j=state.player_state(1,id_player).position
        ja=state.player_state(2,id_player).position
        b=state.ball.position
        bf=b+4*state.ball.vitesse
        if(id_team == 1):
            if(b.x>90):
                p1=Vector2D(55,bf.y)
                return SoccerAction(acceleration=p1-j)
            else :
                if(b.x<80) and j.distance(b)>0.65:
                    p=Vector2D(80,j.y)
                    a=SoccerAction(b-j)
                    z=SoccerAction(p-j,p-b)
                    return a+z
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
                return SoccerAction(acceleration=bf-j,shoot=p1-b)
        elif(id_team == 2): 
            if(b.x<90):
                p1=Vector2D(125,bf.y)
                return SoccerAction(acceleration=p1-ja)
                
            else:
                if b.x>100 and ja.distance(b)>0.65:
                    p=Vector2D(100,ja.y)
                    a=SoccerAction(b-ja)
                    z=SoccerAction(p-ja,p-b)
                    return a+z
                    
                    
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
                return SoccerAction(acceleration=bf-ja,shoot=p1-b)
team1 = SoccerTeam(name="Team 1")
team2 = SoccerTeam(name="Team 2")

# Add players
team1.add("Player 1", firstrat())  # Random strategy
team2.add("Player 2", firstrat())   # Random strategy

# Create a match
simu = VolleySimulation(team1, team2)

# Simulate and display the match
volley_show_simu(simu)