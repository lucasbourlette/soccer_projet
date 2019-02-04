#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 16:29:58 2019

@author: 3672216
"""

from projet import FonceurStrategy, DefenseStrategy
from soccersimulator import SoccerTeam

def get_team(nb_players):
    team = SoccerTeam(name = "Lucas's Team")
    if nb_players == 1:
        team.add("Stirker", FonceurStrategy())
    if nb_players == 2:
        team.add("Stirker", FonceurStrategy())
        team.add("Random", DefenseStrategy())
    return team

if __name__ == '__main__':
    from soccersimulator import Simulation, show_simu
    
    team1 = get_team(1)
    team2 = get_team(2)
    
    simu = Simulation(team1, team2)
    
    show_simu(simu)