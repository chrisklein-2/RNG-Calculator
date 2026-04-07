import math

gray_chin_caught = 1601
gray_chin_chance = 1/128920
red_chin_caught = 6604
red_chin_chance = 1/95373

chance1 = math.exp(gray_chin_caught * math.log(1 - gray_chin_chance))
chance2 = math.exp(red_chin_caught * math.log(1 - red_chin_chance))

chance = (1 - (chance1 * chance2)) * 100

print(f"Chance of getting the drop at {gray_chin_caught+red_chin_caught} kill count: {chance:.2f}%")

p1 = math.exp(5000 * math.log(1-(1/500)))
print(1-p1)