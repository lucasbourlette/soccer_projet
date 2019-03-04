#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 11:49:25 2019

@author: 3672216
"""
from mbappepresident.projet import FonceurStrategy, DefenseStrategy,Fonceur2Strategy
from soccersimulator import SoccerTeam

def get_team(nb_players):
    team = SoccerTeam(name = "Lucas's Team")
    if nb_players == 1:
        team.add("mitroglou", Fonceur2Strategy())
    if nb_players == 2:
        team.add("mitroglou", Fonceur2Strategy())
        team.add("Kante", DefenseStrategy())
    return team