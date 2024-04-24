# Importing Required Libraries
import numpy as np
import random
import math
import copy

class MDP():
    def __init__(self, Patients):
        self.Patients = Patients
        self.Patient_count = len(Patients)
        self.time = 10
        self.doctors = 2
        self.Appointment_slots = []
        self.time_slots = 8
        self.Q = [[[0,0]] * (self.Patient_count) for _ in range(self.time_slots + 1)]
        self.actions = []
        

    def Epsilon(self,epi,max_epi):
        temp = 10 * (epi - 0.5 * max_epi)/ max_epi
        return (0.5)/(1 + pow(math.e,temp))
        
    def State(self):
        state = self.Patients[self.Patient_count]
        self.Patient_count += 1
        print(state)
        return state 

    def Actions(self):
        actions = []
        self.reset()
        for pat in self.Patients:
            for i in range(len(self.Appointment_slots)):
                for j in range(len(self.Appointment_slots[i])):
                    actions.append((i, pat[0], pat[1], self.time + j))
        self.actions = actions

    def Best_Action(self,action):
        best_action = action[0]
        max_reward = -(abs(action[0][2] - action[0][3]))
        for i in action:
            if -(abs(i[2] - i[3])) > max_reward:
                best_action = i
                max_reward = -(abs(i[2] - i[3]))
        return (best_action,max_reward)

    def Remove_Actions(self,p_id,d_id,time,action):
        for k in range(len(action)-1,-1,-1):
            i = action[k]
            if (i[1] == p_id or (i[0] == d_id and i[3] == time)):
                action.remove(i)
        return action

    def reset(self):
        self.Appointment_slots = [[0] * (self.time_slots//self.doctors) for _ in range(self.doctors)]
             
    def Action_Selection(self,action,episode,max_episodes):
        if (len(action) == 0):
            return
        epsilon = self.Epsilon(episode,max_episodes)
        if random.uniform(0, 1) < epsilon:
            random.seed(42)
            state = random.choice(action)
            return state,-(abs(state[2] - state[3]))
        else:
            return self.Best_Action(action)
        
    def Q_learning(self):
        # Initializing Hyperparameters
        alpha = 0.5
        gamma = 0.9
        max_episodes = 100
        num_state = self.time_slots + 1
        for episode in range(max_episodes):
            self.reset()
            action = copy.deepcopy(self.actions)
            state = 0
            while True: 
                temp = self.Action_Selection(action,episode,max_episodes)
                act,reward = temp[0],temp[1]
                i , j = state,act[1]-1

                new_state = state + 1 

                #Bellman's Equation
                temp1 = self.Q[i][j][0]
                Max = max(self.Q[new_state])

                self.Q[i][j][0] = temp1 + alpha * (reward + (gamma * Max[0]) - temp1)

                self.Appointment_slots[act[0]][act[3]-self.time] = copy.deepcopy(act)
                self.Q[i][j][1] = copy.deepcopy(self.Appointment_slots)

                action = self.Remove_Actions(act[1],act[0],act[3],action)
                state = new_state
                if new_state == num_state - 1:
                    break



   
    
   
