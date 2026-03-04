# -*- coding: utf-8 -*-
"""
Created on Tue Feb  24 16:58:45 2026

@author: aidan
"""

# -*- coding: utf-8 -*-
"""
Programming Lab 3 – Grass / Sheep / Wolves Replicator Model
@author: aidan
"""

import numpy as np
import matplotlib.pyplot as plt

def percent(x, total):
    if total == 0:
        return 0.0
    return x / total

def sheep_eat_grass(grass, sheep, grass_per_sheep):
    #Each sheep needs grass_per_sheep units of grass to survive this step.
    #Returns: sheep_fed, grass_left
    
    if sheep <= 0 or grass <= 0:
        return 0, grass

    #max sheep that can be fed
    max_fed = int(grass / grass_per_sheep)
    sheep_fed = min(sheep, max_fed)

    grass_used = sheep_fed * grass_per_sheep
    grass_left = grass - grass_used
    return sheep_fed, grass_left

def wolves_eat_sheep(wolves, sheep, wolf_success):
    #Each wolf can eat at most 1 sheep per step.
    #olf_success controls how many wolves actually succeed (0 to 1-ish).
    #Returns: wolves_fed, sheep_left
    if wolves <= 0 or sheep <= 0:
        return 0, sheep
    #Determines the success rate!
    wolves_fed = int(wolves * wolf_success)

    #This makes it so that wovles can't eat more sheep than exists :)
    wolves_fed = min(wolves_fed, wolves, sheep)

    sheep_left = sheep - wolves_fed
    return wolves_fed, sheep_left

#Decided these'll be my starting standards I decided to do intervals of 4
steps = 400

Grass = 120.0
Sheep = 60
Wolves = 12

#Grass
grass_regen = 15.0
grass_cap = 250.0

#Sheep 
grass_needed = 1.0        # grass units needed per sheep per step
sheep_birth_rate = 0.18   #Random fraction number for reproducing

#Wolf
wolf_success = 0.55       # fraction of wolves that successfully eat each step
wolf_birth_rate = 0.25    #same thing but for wolves

print("Grass / Sheep / Wolves Model")
print("Grass regenerates each step (capped).")
print("Sheep must eat grass to survive; fed sheep can reproduce.")
print("Wolves must eat sheep to survive; fed wolves can reproduce.\n")

#PLOTTING!!! THE MOST ANNOYING PART IN MY OPINION TOOK FOREVER TO FIGURE OUT.
grass_hist = []
sheep_hist = []
wolves_hist = []

r_grass = []
r_sheep = []
r_wolves = []


for i in range(steps):

    #Grass grows back
    Grass = Grass + grass_regen
    if Grass > grass_cap:
        Grass = grass_cap

    #Sheep will eat grass
    sheep_fed, Grass = sheep_eat_grass(Grass, Sheep, grass_needed)

    #sheeps that didn't eat die
    Sheep = sheep_fed

    #sheep eat and can reproduce
    sheep_babies = int(sheep_fed * sheep_birth_rate)
    Sheep = Sheep + sheep_babies

    #Wolves can eat sheep
    wolves_fed, Sheep = wolves_eat_sheep(Wolves, Sheep, wolf_success)

    #wolves that don't eat die
    Wolves = wolves_fed

    # wolves ate are able to reproduce
    wolf_babies = int(wolves_fed * wolf_birth_rate)
    Wolves = Wolves + wolf_babies

    #Annoying part. This saves everything
    grass_hist.append(Grass)
    sheep_hist.append(Sheep)
    wolves_hist.append(Wolves)

    total = Grass + Sheep + Wolves  # simple normalization for "relative"
    r_grass.append(percent(Grass, total))
    r_sheep.append(percent(Sheep, total))
    r_wolves.append(percent(Wolves, total))

#PRINTS
print("Final values after", steps, "steps:")
print("Grass =", Grass)
print("Sheep =", Sheep)
print("Wolves =", Wolves)

plt.figure()
plt.plot(r_grass, label="Grass (relative)")
plt.plot(r_sheep, label="Sheep (relative)")
plt.plot(r_wolves, label="Wolves (relative)")

plt.xlabel("Step")
plt.ylabel("Relative Amount")
plt.title("Grass / Sheep / Wolves: Relative Amounts vs Step")
plt.legend()
plt.grid(True)
plt.show()
#Honestly don't know why the graph looks like that but HEY, it workS!