import numpy as np
import time

"""
    No longer need storage.py as we are using numpy to generate the dataset and calculate the probabilities on the fly, instead of storing them in a json file. 
    This allows for much faster execution and more flexibility in analyzing the data. (5 seconds to .1 seconds for 1024 RNG value with 10,000 simulations)
    Next step is to create interface using tkinter.
"""

# Gets user input for RNG value and current kill count
def get_input():
    input_rng = input("Enter an RNG value > ")
    drop_rate = int(input_rng)
    input_kc = input("Enter current kill count > ")
    kill_count = int(input_kc)
    return drop_rate, kill_count

# Performs the calculation to determine the probability of getting the drop at the current kill count.
def perform_calculation(drop_rate):
    probability = 1/drop_rate
    rng = np.random.default_rng()
    dataset = rng.geometric(p=probability, size=10000)
    return dataset

# Prints the results of the calculation.
def print_results(drop_rate, kill_count, dataset):
    successes_at_kill_count = dataset <= kill_count
    print(f"At {kill_count}/{drop_rate}: {np.mean(successes_at_kill_count)*100:.2f}% of players received the drop")
    return np.mean(successes_at_kill_count)*100

if __name__ == "__main__":

    drop_rate, kill_count = get_input()

    start_time = time.perf_counter()

    dataset = perform_calculation(drop_rate)

    print_results(drop_rate, kill_count, dataset)

    end_time = time.perf_counter()

    print(f"Execution time: {end_time - start_time:.2f} seconds")