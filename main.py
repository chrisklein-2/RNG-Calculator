from storage import load

def print_data(data):
    """Prints data in a readable format."""
    for val, key in data.items():
        rng = int(val[10:])
        print(f"\nDrop rate: {rng}\n")
        rng//=4
        for milestone, percentage in key.items():
            if not milestone == "All Simulations":
                print(f"{milestone} ({rng}): {percentage:.2f}%")
            rng *= 2

def print_custom(data, rng_value, current):
    """Prints custom data based on current and rng_value."""
    rng_value = f"rng_value: {rng_value}"
    if rng_value in data:
        print(f"\n{rng_value}\n")
        total = 0
        for i in data[rng_value]["All Simulations"]:
            total += 1
            if i >= current:
                total /= 100
                print(f"{int(total * 100)} players got it by {current} out of 10000: {total:.2f}% to have gotten it by now.")
                break
    else:
        print(f"No data found for RNG value: {rng_value}")

def print_specific(data, rng_value):
    """Prints data for a specific RNG value."""
    if str(rng_value) in data:
        print(f"\nRNG Value: {rng_value}\n")
        for milestone, percentage in data[str(rng_value)].items():
            if not milestone == "All Simulations":
                print(f"{milestone} : {percentage:.2f}%")
    else:
        print(f"No data found for RNG value: {rng_value}")

if __name__ == "__main__":
    data = load("drop_rate_results.json")
    
    input_value = input("Enter an RNG value to view specific results, Press Enter to view all, Press 0 for custom results > ")
    
    if input_value == "0" or input_value == "":
        if input_value == "0":
            rng_value = int(input("Enter RNG value > "))
            current = int(input("Enter current kill count > "))
            print_custom(data, rng_value, current)
        else:
            print_data(data)
    else:
        try:
            rng_value = f"rng_value:{input_value}"
            print_specific(data, rng_value)
        except ValueError:
            print_data(data)