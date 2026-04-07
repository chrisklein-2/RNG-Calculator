import math


def perform_chin_calculation(gray_chin_caught, red_chin_caught):
    gray_chin_chance = 1/128920
    red_chin_chance = 1/95373

    chance1 = math.exp(gray_chin_caught * math.log(1 - gray_chin_chance))
    chance2 = math.exp(red_chin_caught * math.log(1 - red_chin_chance))

    chance = (1 - (chance1 * chance2)) * 100

    print(f"Chance of getting the drop at {gray_chin_caught+red_chin_caught} chins caught: {chance:.2f}%")


if __name__ == "__main__":

    while True:
        try:
            gray_chin_caught = int(input("Enter the number of gray chinchompas caught > "))
            red_chin_caught = int(input("Enter the number of red chinchompas caught > "))
            break
        except ValueError:
            print("Please enter valid integers for the number of chinchompas caught.")

    perform_chin_calculation(gray_chin_caught, red_chin_caught)