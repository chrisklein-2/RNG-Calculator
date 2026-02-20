import json
import re

def save(data, filename):
    """Saves data to a JSON file."""
    with open(filename, 'w') as f:
        json_string = json.dumps(data, indent=4)
        json_string = re.sub(r'\[\s*(.*?)\s*\]', 
                        lambda m: '[' + re.sub(r'\s+', ' ', m.group(1)) + ']', 
                        json_string, flags=re.DOTALL)
        f.write(json_string)

def load(filename):
    """Loads data from a JSON file."""
    with open(filename, 'r') as f:
        return json.load(f)
    
