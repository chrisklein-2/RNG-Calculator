import numpy as np
from collections import Counter
def run_simulation(rng_value=512, num_simulations=10000):
    """
    Simulate a 1/rng drop rate across multiple trials.
    Returns an array of attempt counts and the rng value used.
    """
    # Geometric distribution: number of rolls until first "drop"
    # Replaces the slow per-simulation while loop with a single vectorized call
    simulations = np.random.geometric(p=1 / rng_value, size=num_simulations)
    return simulations, rng_value
def milestones(sims, rng):
    """
    Count how many simulations completed within key attempt thresholds.
    Also returns a frequency map of all individual results.
    """
    # Sort without mutating the original array
    sorted_sims = np.sort(sims)
    # Define thresholds as fractions/multiples of the base drop rate
    thresholds = {
        "Quarter Drop Rate": rng // 4,
        "Half Drop Rate": rng // 2,
        "Drop Rate": rng,
        "Double Drop Rate": rng * 2,
        "Triple Drop Rate": rng * 3,
        "Quadruple Drop Rate": rng * 4,
    }
    # Binary search to count how many sims finished within each threshold
    results = {}
    for name, threshold in thresholds.items():
        results[name] = int(np.searchsorted(sorted_sims, threshold, side="right"))
    # Frequency count of every attempt value
    results["All Simulations"] = dict(Counter(sorted_sims.tolist()))
    return results
sims, rng_value = run_simulation(1000000000)

results = milestones(sims, rng_value)

print(f"sims: {max(sims)} rng_value: {rng_value}")

print(f"Results: {results}")