#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 17:10:49 2019

@author: 3672216
"""

from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam, Simulation, show_simu

from soccersimulator import settings


class MyState(object):
    def __init__(self,state,idteam,idplayer):
        self.state = state
        self.id_team=idteam
        self.id_player= idplayer
        self.key = (idteam,idplayer)
    
    @property
    def ball_vitesse(self):
        return self.state.ball.vitesse
    
    @property
    def liste_opposant(self):
        return [self.state.player_state(id_team, id_player).position for (id_team, id_player) in self.state.players if id_team != self.id_team]
    
    @property
    def opposant_le_plus_proche(self):
        opp=self.liste_opposant()
        return min([(self.player.distance(player),player)for player in opp])
    
    
#====================================================================================================================================
#        Position
    @property
    def my_position(self):
      return self.state.player_state(self.id_team,self.id_player).position

    @property
    def ball_position(self):
        return self.state.ball.position
    
    @property
    def ball_position_futur(self):
         return self.ball_position+ 5 * self.ball_vitesse

    @property
    def distance_balle (self): 
        return self.ball_position.distance(self.player)
    
    @property
    def distance_balle_adv_proche(self):
        return self.ball_position.distance(opposant_le_plus_proche(self))
    
    @property    
    def adv_plus_proche_ball(self):
        opp = liste_opposant
        return min([(self.ball_position.distance(player),player)for player in opp])
        
    @property
    def goal(self):
       return  Vector2D((2-self.id_team)*settings.GAME_WIDTH,settings.GAME_HEIGHT/2.)
   
    @property
    def tire_vers_but(self):
        return SoccerAction(self.ball_position_futur - self.my_position, self.goal-self.ball_position)
    
    @property
    def cour_vers_ballon(self):
        return SoccerAction(self.ball_position_futur - self.my_position)
        
    
    