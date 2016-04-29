# This file is written for you tto generate random chests.
# Do not modify this file at all.

import random

def generate():
  ''' Randomly generates a list that represents a treasure chest. '''
  
  chest = []
  types = [int, int, float, float, str, str, bool, bool, list]
  
  for i  in range(random.randint(1, 5)):
    currentType = random.choice(types)
    if currentType == int:
      chest.append(random.randint(-5, 10))
    elif currentType == float:
      chest.append(random.uniform(-5, 10))
    elif currentType == bool:
      chest.append(random.choice([True, False]))
    elif currentType == str:
      chest.append(random.choice(["seaweed", "lobster", "saltwater", "sand"]))
    elif currentType == list:
      chest.append(generate())
  
  return chest
