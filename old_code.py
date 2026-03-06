import random 
import io
import time
from storage import save, load
def simulate_drop_rate(rng: int):
    
    found = False
    total = 0
    while not found:
        roll = random.randint(1, rng)
        total += 1
        if roll == 1:
            found = True

    return total

def milestones(sims: list, rng: int):
    sims.sort()
    
    milestones = {'Quarter Drop Rate': 0,
                  'Half Drop Rate': 0,
                  'Drop Rate': 0,
                  'Double Drop Rate': 0,
                  'Triple Drop Rate': 0,
                  'Quadruple Drop Rate': 0}
    half_rate = rng // 2
    quarter_rate = rng // 4
    double_rate = rng * 2
    triple_rate = rng * 3
    quadruple_rate = rng * 4
    final_sims = {}
    for i, sim in enumerate(sims):
        if sim > quarter_rate and milestones['Quarter Drop Rate'] == 0:
            milestones['Quarter Drop Rate'] = i
        if sim > half_rate and milestones['Half Drop Rate'] == 0:
            milestones['Half Drop Rate'] = i
        if sim > rng and milestones['Drop Rate'] == 0:
            milestones['Drop Rate'] = i
        if sim > double_rate and milestones['Double Drop Rate'] == 0:
            milestones['Double Drop Rate'] = i
        if sim > triple_rate and milestones['Triple Drop Rate'] == 0:
            milestones['Triple Drop Rate'] = i
        if sim > quadruple_rate and milestones['Quadruple Drop Rate'] == 0:
            milestones['Quadruple Drop Rate'] = i
        final_sims[sim] = final_sims.get(sim, 0) + 1
    milestones['All Simulations'] = final_sims
    return milestones

def run_simulation(rng_value = 512):
     
    num_simulations = 10000
    simulations = []
    for _ in range(num_simulations):
        attempts = simulate_drop_rate(rng_value)
        simulations.append(attempts)
    return simulations, rng_value

if __name__ == "__main__":
    print("Running simulations...")
    
    start_time = time.perf_counter()

    sims, rng_value = run_simulation(1024)

    end_time = time.perf_counter()
    print(f"Simulations completed in {end_time - start_time:.2f} seconds")

"""
    rng = 2
    rng_records = {}
    for _ in range(10):
        rng *= 2
        simulations, rng_value = run_simulation(rng_value=rng)
        
        average_attempts = sum(simulations) / len(simulations)
        milestone_results = milestones(simulations, rng_value)
        print(f"\nRNG Value: {rng_value}")
        rng_records[f"rng_value: {rng_value}"] = milestone_results
        for key, value in milestone_results.items():
            if key != "All Simulations":
                milestone_results[key] = value / len(simulations) * 100
                print(f"{key}: {milestone_results[key]:.2f}%")
        
    save(rng_records, "drop_rate_results.json")
"""