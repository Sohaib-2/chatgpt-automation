import os
import csv
import datetime

def save_to_csv(data, filepath):
    # Ensure filepath is not None
    if not filepath:
        filepath = "data/outputs/responses.csv"
        print(f"No output path specified, using default: {filepath}")
    
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    
    # Check if file exists to determine if we need headers
    file_exists = os.path.isfile(filepath)
    
    with open(filepath, 'a', newline='', encoding='utf-8') as f:
        fieldnames = ['timestamp', 'type', 'prompt', 'response']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        
        # Write header if file doesn't exist
        if not file_exists:
            writer.writeheader()
        
        # Write each data row
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        for item in data:
            writer.writerow({
                'timestamp': timestamp,
                'type': item['type'],
                'prompt': item['prompt'],
                'response': item['response']
            })
            
    return True

def save_to_env_file(data_dict):
    """
    Save or update key-value pairs in .env file
    
    Args:
        data_dict (dict): Dictionary of key-value pairs to save
    """
    # Read existing .env file if it exists
    env_data = {}
    if os.path.exists(".env"):
        with open(".env", "r") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    key, value = line.split("=", 1)
                    env_data[key] = value
    
    # Update with new values
    env_data.update(data_dict)
    
    # Write back to .env file
    with open(".env", "w") as f:
        for key, value in env_data.items():
            f.write(f"{key}={value}\n")
    
    return True

def create_directories():
    directories = [
        'data/outputs',
        'data/cookies'
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)