# Sailing Simulator
# - https://github.com/topics/sailing-simulator
# - Simple sailing simulator from https://github.com/PPierzc/ai-learns-to-sail
#   - https://github.com/PPierzc/ai-learns-to-sail/blob/master/tasks/channel.py
import numpy as np

class Engine:
    """Defines the environment function from the generator engine.
       Expects the following:
        - reset() to reset the env a start position(s)
        - step() to make an action and update the game state
        - legal_moves_generator() to generate the list of legal moves
    """
    def __init__(self) -> None:
        """Initialize Engine"""
        self.Environment = "Engine Initialization"

    # --------------------------
    # Defined functions used by engine source
    @staticmethod
    def vel(theta, theta_0=0, theta_dead=np.pi / 12):
        return 1 - np.exp(-(theta - theta_0) ** 2 / theta_dead)
    
    @staticmethod
    def rew(theta, theta_0=0, theta_dead=np.pi / 12):
        return Engine.vel(theta, theta_0, theta_dead) * np.cos(theta)
    # --------------------------

    def reset(self):
        """Fully reset the environment."""
        #obs, _ = self.Environment.reset()
        self.x = np.random.uniform(-9.9, 9.9)
        self.angle = 0  # always start with angle 0
        self.y = 0
        obs = str(self.x)+'_'+str(self.angle)
        return obs

    
    def step(self, state:any, action:any):
        """Enact an action."""
        # In problems where the agent can choose to reset the env
        if (state=="ENV_RESET")|(action=="ENV_RESET"):
            self.reset()
            
        a = [-0.1, 0.1][action]

        # Observation space
        self.x += (Engine.vel(self.angle + a) * np.sin(self.angle + a))
        self.y += (Engine.vel(self.angle + a) * np.cos(self.angle + a))
        self.angle += a
        obs = str(self.x)+'_'+str(self.angle)
        
        # Reward signal
        reward = Engine.rew(self.angle)

        # Termination signal
        # - Source: Terminal only on hitting piers/walls, otherwise continues to action limiit
        # - Update: Add terminal state if y > 25 (or another arbirary value)
        if np.abs(self.x)>10:
            reward = -1
            terminated = True
        elif np.abs(self.y)>25:
            reward = 1
            terminated = True
        else:
            terminated = False
        
        return obs, reward, terminated

    def legal_move_generator(self, obs:any=None):
        """Define legal moves at each position"""
        # Action space: [0,1] for turn slightly left or right
        # - Kept as binary but might be better as continuous [-0.1, 0.1]
        legal_moves = [0, 1]
        return legal_moves

