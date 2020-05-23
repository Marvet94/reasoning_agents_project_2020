if __name__ == '__main__':
    # This is a terrible hack just to be able to execute this file directly
    import sys
    sys.path.insert(0, '../')

from worlds.game_objects import *
from worlds.grid_world import GridWorldParams, GridWorld, run_human_agent
import random, math, os
import numpy as np

class WaiterWorld(GridWorld):

    def __init__(self, params):
        super().__init__(params)

    def _get_reward_and_gameover(self):
        # returns the reward and whether the game is over
        # NOTE: This domain has no game over
        if "3" in self.get_events() and "C" not in self.get_events():#if agent is in the main room and there is no clients -> game over
            return 1, True 
        return 0, False

    def get_events(self):
        """
        Returns the string with the propositions that are True in this state
        """
        ret = "" 

        # adding the id of the current room
        room_agent = self._get_room(self.agent.i, self.agent.j)
        ret += str(room_agent)

        if self.agent.is_carrying_order():
            ret += "*" # means that the agent is carrying the order

        for o in self.orders:
            if o.in_map and room_agent == self._get_room(o.i,o.j):
                ret += "O" # means that the agent is at the same room than a order
        
        for c in self.clients:
            if c.in_map and room_agent == self._get_room(c.i,c.j):
                ret += "C" # means that the agent is at the same room than a client

        return ret


    def get_all_events(self):
        """
        Returns a string with all the possible events that may occur in the environment
        """
        return "0123*OC"

    def get_map_classes(self):
        """
        Returns the string with all the classes of objects that are part of this domain
        """
        return "OC"

    def _get_features_pos_and_dims(self):
        a = self.agent
        room_agent = self._get_room(a.i, a.j)
        
        # adding position of the agent
        dims = [self.max_i, self.max_j]
        pos  = [a.i, a.j]

        # adding whether it has an order
        dims.append(2)
        pos.append(int(a.is_carrying_order()))
        
        # adding whether there are keys in the current room
        no_orders = True
        for o in self.orders:
            if room_agent == self._get_room(o.i,o.j):
                dims.append(2)
                pos.append(int(o.in_map))
                no_orders = False
        if no_orders:
            dims.extend([2,2])
            pos.extend([0,0])            
        
        # adding whether there are clients in the current room
        for c in self.clients:
            dims.append(2)
            pos.append(int(c.in_map and room_agent == self._get_room(c.i,c.j))) 
        
        return pos, dims

    def _load_map(self, file_map):
        # loading a map from the set of possible maps
        super()._load_map(file_map)

        # adding problem-specific attributes
        self.orders = []
        self.clients = []
        for row in self.map:
            for obj in row:
                if str(obj) == 'O': self.orders.append(obj) 
                if str(obj) == 'C': self.clients.append(obj)

        for o in self.orders:
        	o.in_map=False

        for c in self.clients:
        	c.add_orders(self.orders)#gives to the clients  the "menu"
		
    def get_optimal_action(self):
        return None
    def get_perfect_rm(self):
    	#RM FROM COOKIE
        # NOTE: This is used for debugging purposes and to compute the expected reward of an optimal policy
        delta_u = {}
        delta_u[(0, '3B')] = 1
        delta_u[(1, '0c')] = 2
        delta_u[(1, '2')]  = 2
        delta_u[(1, '2c')] = 3
        delta_u[(1, '0')]  = 3
        delta_u[(2, '3B')] = 1
        delta_u[(2, '0C')] = 0
        delta_u[(3, '3B')] = 1
        delta_u[(3, '2C')] = 0
        return delta_u

# This code allow to play a game (for debugging purposes)
if __name__ == '__main__':
    file_map = "../../maps/waiter.txt"
    game_type = "waiterworld"
    max_time = 5000
    num_total_steps = 1000000
    num_steps = 0

    params = GridWorldParams(game_type, file_map, 0)
    while num_steps < num_total_steps:
        game = WaiterWorld(params)
        reward,steps,trace = run_human_agent(game, max_time)
        num_steps += steps