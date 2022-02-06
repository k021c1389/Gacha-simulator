import numpy as np

def pickup(weight):
  """重みに応じてガチャを回す"""
  rarities = ["N", "N+", "R", "R+", "SR", "SR+"]
  picked_rarity = np.random.choice(rarities, p=weight)
  item = np.random.randint(1, 11)
  return { "rarity": picked_rarity, "item": item }

def single_gacha():
  weight = [0.33, 0.25, 0.20, 0.15, 0.05, 0.02]
  result = []

  result.append(pickup(weight))

  return result

def eleven_gacha():
  weight = [0, 0, 0.57, 0.3, 0.1, 0.03]
  result = []
  
  for i in range(0,10):
    result.append(pickup(weight))

  last_one = pickup([0, 0, 0, 0, 1, 0])  
  result.append(last_one)

  return result

if __name__ == "__main__":
  print(single_gacha())
  print(eleven_gacha())
