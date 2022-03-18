#Author: Bernardo Calvo

import copy
import random

class Hat:
  def __init__(self, **kwargs):
    self.contents = convert_list(kwargs.items())

  def draw(self, nballs):
    if nballs >= len(self.contents):
      return self.contents
    res = list()
    for i in range(nballs):
      ball = random.choice(self.contents)
      res.append(ball)
      self.contents.remove(ball)
    return res
    
def convert_list(dict):
  res = list()
  for color,value in dict:
    for i in range(value):
      res.append(color)
  return res

def check_sucess(expected, result):
  for color,value in expected.items():
    if result.count(color) < value:
      return False
  return True
  
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  nsucess = 0
  for exp in range(num_experiments):
    copyhat = copy.deepcopy(hat)
    result = copyhat.draw(num_balls_drawn)
    if check_sucess(expected_balls, result):
      nsucess += 1
  return nsucess/num_experiments

#Example
random.seed(95)
hat = Hat(blue=4, red=2, green=6)
probability = experiment(
    hat=hat,
    expected_balls={"blue": 2,
                    "red": 1},
    num_balls_drawn=4,
    num_experiments=2000)
print("Probability:", probability)