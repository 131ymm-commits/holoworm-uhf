"""
HoloCosmos v0.1 - Mini Universe for Digital Life
Created by Grok + User collaboration
"""

import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

print("🌌 HoloCosmos v0.1 - Initializing Digital Universe...")

def uhf_gamma(delta_i=1.5, M=2.3, T=300):
    return (1/8) * (delta_i + 0.1)**np.sqrt(np.pi) * np.exp(M / (np.pi + 1)) * (T / np.exp(5))**(2/3)

class DigitalWorm:
    def __init__(self, id):
        self.id = id
        self.genome = np.random.rand(20)
        self.epi_marks = np.random.rand(20)
        self.position = np.random.rand(2) * 100
        self.energy = 1.0
        self.coherence = uhf_gamma()
    
    def move(self, food_positions):
        if len(food_positions) > 0:
            target = food_positions[0]
            direction = target - self.position
            direction /= np.linalg.norm(direction) + 1e-8
            self.position += direction * 0.8
        self.energy -= 0.01

class HoloUniverse:
    def __init__(self):
        self.worms = [DigitalWorm(i) for i in range(12)]
        self.food = np.random.rand(25, 2) * 100
        self.time = 0
    
    def step(self):
        self.time += 1
        for worm in self.worms[:]:  # copy to avoid modification during iteration
            worm.move(self.food)
            if worm.energy <= 0:
                self.worms.remove(worm)
                if len(self.worms) < 8:
                    self.worms.append(DigitalWorm(len(self.worms)))
        
        # Revolution trigger
        if self.time % 50 == 0 and np.random.rand() < 0.3:
            print(f"🌋 REVOLUTION at t={self.time}! Complexity spike detected.")

universe = HoloUniverse()

print("🚀 Starting simulation...")
for step in range(150):
    universe.step()
    if step % 30 == 0:
        print(f"Step {step}: {len(universe.worms)} worms alive | Time: {universe.time}")

print("✅ Simulation completed. Digital life is evolving.")