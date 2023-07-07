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
    def __init__(self, supervised_rewards:str="True") -> None:
        """Initialize Engine"""
        #self.Environment = "Engine Initialization"
        self.x_limit = 10
        self.y_limit = 25
        self.angle_limit = np.pi / 2
        self.supervised_rewards = supervised_rewards
        # [-10~-9, -9~-7, -7~-3, -3~-1, -1~1, 1~3, 3~7, 7~9, 9~10]
        self.x_checker = [False, False, False, False, False, False, False, False, False, False]
    # --------------------------
    # Defined functions used by engine source
    @staticmethod
    def vel(theta, theta_0=0, theta_dead=np.pi / 12):
        return 1 - np.exp(-(theta - theta_0) ** 2 / theta_dead)
    
    @staticmethod
    def rew(theta, theta_0=0, theta_dead=np.pi / 12):
        return Engine.vel(theta, theta_0, theta_dead) * np.cos(theta)
    # --------------------------

    def reset(self, start_obs:str=None):
        """Fully reset the environment."""
        # Allow reset to be at fixed start position or random
        if start_obs:
            self.x = np.round(float(start_obs.split('_')[0]),4)
            self.angle = np.round(float(start_obs.split('_')[1]),1)
        else:
            self.x = 0 #np.round(np.random.randint(-9.9, 9.9),4) # Changed to rand_int to reduce num of start states
            self.angle = 0  # always start with angle 0
        self.y = 0
        obs = "{:0.4f}".format(self.x)+'_'+"{:0.1f}".format(self.angle)
        return obs

    
    def step(self, state:any, action:any):
        """Enact an action."""
        a = [-0.1, 0.1][action]
        # Observation space
        self.x += np.round((Engine.vel(self.angle + a) * np.sin(self.angle + a)),4) # Round x to 2dp
        # Exploration X position checking
        if ((self.x)<-9):
            if (self.x_checker[0]==False):
                print(" ")
                print("x = ",self.x)
                self.x_checker[0] = True
                print(self.x_checker)
        elif ((self.x)<-7):
            if (self.x_checker[1]==False):
                print(" ")
                print("x = ",self.x)
                self.x_checker[1] = True
                print(self.x_checker)
        elif ((self.x)<-3):
            if (self.x_checker[2]==False):
                print(" ")
                print("x = ",self.x)
                self.x_checker[2] = True
                print(self.x_checker)
        elif ((self.x)<-1):
            if (self.x_checker[3]==False):
                print(" ")
                print("x = ",self.x)
                self.x_checker[3] = True
                print(self.x_checker)
        elif ((self.x)<0):
            if (self.x_checker[4]==False):
                print(" ")
                print("x = ",self.x)
                self.x_checker[4] = True
                print(self.x_checker)
        elif ((self.x)<1):
            if (self.x_checker[5]==False):
                print(" ")
                print("x = ",self.x)
                self.x_checker[5] = True
                print(self.x_checker)
        elif ((self.x)<3):
            if (self.x_checker[6]==False):
                print(" ")
                print("x = ",self.x)
                self.x_checker[6] = True
                print(self.x_checker)
        elif ((self.x)<7):
            if (self.x_checker[7]==False):
                print(" ")
                print("x = ",self.x)
                self.x_checker[7] = True
                print(self.x_checker)
        elif ((self.x)<9):
            if (self.x_checker[8]==False):
                print(" ")
                print("x = ",self.x)
                self.x_checker[8] = True
                print(self.x_checker)
        elif ((self.x)<10):
            if (self.x_checker[9]==False):
                print(" ")
                print("x = ",self.x)
                self.x_checker[9] = True
                print(self.x_checker)

        self.y += np.round((Engine.vel(self.angle + a) * np.cos(self.angle + a)),4) # Round y to 2dp
        self.angle = np.round(self.angle+a,1) 
        #obs = str(self.x)+'_'+str(self.angle)
        obs = "{:0.4f}".format(self.x)+'_'+"{:0.1f}".format(self.angle) # fix - https://docs.python.org/3.4/library/string.html#format-specification-mini-language

        # Reward signal
        # - Added flag for whether we give agent immediate positive reward
        # - Update: Added scale factor if using supervised rewards to not override goal rewards
        if self.supervised_rewards=="True":
            reward = Engine.rew(self.angle)/10
        else:
            reward = 0

        # Termination signal
        # - Source: Terminal only on hitting piers/walls, otherwise continues to action limit
        # - Update: Add terminal state if y > 25 (or another arbitrary value)
        # - Update: Limit angle to [-90,90] degrees (i.e. no backwards sailing)
        if np.abs(self.x)>self.x_limit:
            reward = -1
            terminated = True
        elif np.abs(self.y)>self.y_limit:
            reward = 1
            terminated = True
        elif np.abs(self.y)<0:
            reward = -1
            terminated = True
        elif np.abs(self.angle)>self.angle_limit:
            print("Angle limit reached")
            reward = -1
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

