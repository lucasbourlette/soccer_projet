#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 16:29:58 2019

@author: 3672216
"""

from projet import FonceurStrategy, DefenseStrategy
from soccersimulator import SoccerTeam
from mbappepresident import get_team

team1 = SoccerTeam(name="Team 1")
team2 = SoccerTeam(name="Team 2")

# Add players
#team1.add("Random", RandomStrategy()) 
team2.add("manel", DefenseStrategy())  # Random strategy
team1.add("zizou", FonceurStrategy())   # Static strategy

