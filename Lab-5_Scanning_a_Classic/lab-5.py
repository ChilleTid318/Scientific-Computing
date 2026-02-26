# -*- coding: utf-8 -*-
"""
Created on Sat Feb 21 22:34:19 2026

@author: aidan
"""

import matplotlib.pyplot as plt

with open("frankenstein.txt", "r") as f:
    content = f.readlines()
characters = ["Victor Frankenstein (Victor)", "Victor", "De Lacey", "Henry", "The Creature", "creature", "Agatha", "Caroline", "Old Man De Lacey", "Elizabeth", "Ernest", "Felix", "Henry Clerval (Henry)", "Justine", "William"]

count ={'Victor Frankenstein (Victor)': 0, 'The Creature (creature)': 0, 'Agatha': 0, 'Caroline': 0, 'Old Man De Lacey (De Lacey)': 0, 'Elizabeth': 0, 'Ernest': 0, 'Felix': 0, 'Henry Clerval (Henry)': 0, 'Justine': 0, 'William': 0}

for line in content:
    for character in characters:
        if character in line:
            if character == 'Victor':
                count['Victor Frankenstein (Victor)'] += 1
            elif character == 'creature':
                count['The Creature (creature)'] += 1
            elif character == 'Henry':
                count['Henry Clerval (Henry)'] += 1
            elif character == 'De Lacey':
                count['Old Man De Lacey (De Lacey)'] += 1
            else:
                count[character] += 1
print(count)
           
plt.bar(count.keys(), count.values())
plt.xticks(list(count.keys()), rotation='vertical')

plt.ylabel('Count')
plt.title('Character count')

plt.show()