import psutil
import os
import time
import json

def load_config(config_file="config.json"):
    try:
        with open(config_file, "r") as file:
            config = json.load(file)
        return config
    except FileNotFoundError:
        print(f"Config file '{config_file}' not found.")
        return None
    except json.JSONDecodeError:
        print(f"Config file '{config_file}' is not a valid JSON file.")
        return None

def find_processes_by_name(process_name):
    processes = []
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == process_name:
            processes.append(proc)
    return processes

def monitor_memory_usage(process_name, memory_limit_mb, check_interval=5):
    while True:
        processes = find_processes_by_name(process_name)
        if not processes:
            print(f"No processes with name '{process_name}' found.")
            break

        for process in processes:
            try:
                memory_info = process.memory_info()
                memory_usage_mb = memory_info.rss / (1024 * 1024)  # Convert bytes to MB

                print(f"Process '{process_name}' (PID: {process.pid}) is using {memory_usage_mb:.2f} MB of RAM.")

                if memory_usage_mb > memory_limit_mb:
                    print(f"Process '{process_name}' (PID: {process.pid}) exceeded the memory limit of {memory_limit_mb} MB. Terminating...")
                    process.terminate()
                    process.wait()  
            except psutil.NoSuchProcess:
                continue

        time.sleep(check_interval)

if __name__ == "__main__":
    config = load_config()
    if config:
        process_name = config.get("process_name")
        memory_limit_mb = config.get("memory_limit_mb")
        check_interval = config.get("check_interval", 5)  # Default to 5 seconds

        if process_name and memory_limit_mb:
            print(f"Monitoring process '{process_name}' with a memory limit of {memory_limit_mb} MB.")
            monitor_memory_usage(process_name, memory_limit_mb, check_interval)
        else:
            print("Invalid configuration. Please check the config file.")
    else:
        print("Failed to load configuration.")