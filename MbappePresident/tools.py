#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 17:10:49 2019

@author: 3672216
"""

from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam, Simulation, show_simu

from soccersimulator import settings
import math


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
    def my_positionx(self):
      return self.state.player_state(self.id_team,self.id_player).position.x
  
    @property
    def my_positiony(self):
      return self.state.player_state(self.id_team,self.id_player).position.y

    @property
    def ball_position(self):
        return self.state.ball.position
    @property
    def ball_positionx(self):
        return self.state.ball.position.x
    @property
    def ball_positiony(self):
        return self.state.ball.position.y
    
    @property
    def ball_position_futur(self):
         return self.ball_position+ 5 * self.ball_vitesse

    @property
    def distance_balle (self): 
        return self.ball_position.distance(self.player)
    
    @property
    def distance_balle_adv_proche(self):
        return self.ball_position.distance(self.opposant_le_plus_proche)
    
    @property    
    def adv_plus_proche_ball(self):
        opp = self.liste_opposant
        return min([(self.ball_position.distance(player),player)for player in opp])
        
    @property
    def goal(self):
       return  Vector2D((2-self.id_team)*settings.GAME_WIDTH,settings.GAME_HEIGHT/2.)
   

   
    @property
    def tire_vers_but(self):
        return SoccerAction(self.ball_position_futur - self.my_position, self.goal - self.ball_position_futur)
    
    @property
    def cour_vers_ballon(self):
        return SoccerAction(self.ball_position - self.my_position)
    
    @property
    def norme(self):
        return math.sqrt((self.ball_positionx-self.my_positionx)**2+(self.ball_positiony-self.my_positiony)**2)
    
    @property
    def petit_tire(self):
        
        v1= self.goal-self.my_position
        return v1.normalize()*0.6        
        return SoccerAction(self.ball_position_futur-self.my_position,self.goal-self.ball_position.normalize*0.1)
    
    @property
    def passe(self):
        return SoccerAction(acceleration = Vector2D(), shoot = (self.plus_proche_ami()-self.player))
    @property
    def entreballetbut(self):
        vecteurballbut=Vector2D(((2-self.id_team)*settings.GAME_WIDTH)-self.ball_positionx,settings.GAME_HEIGHT/2.-self.ball_positiony)
        vecteurballjoueur=Vector2D(self.my_positionx-self.ball_positionx,self.my_positiony-self.ball_positiony)
        return SoccerAction(vecteurballbut - vecteurballjoueur)
    
    @property
    def ball_strategy(self):
        if self.id_team_adv() == 2:
            if (self.ball.x>(3*settings.GAME_WIDTH)/4):
                return 0                                                           #Attaque
            else:
                return 1                                                           #Defense
        if (self.id_team_adv() == 1):
            if (self.ball.x<(settings.GAME_WIDTH)/4):
                return 0                                                           #Attaque
            else:
                return 1 
    
    @property
    def peut_shooter(self):
        return self.ball.distance(self.player) < settings.PLAYER_RADIUS + settings.BALL_RADIUS
    
    @property    
    def shoot_ou_cour(self):
        if (self.peut_shooter):
            return self.tire_vers_but
        else:
            return self.cour_vers_ballon 

        return move.to_ball() + shoot.to_goal (self.strength)