# scripts/process_collector.py

import psutil
from datetime import datetime

def collect_processes():
    output_file = "process_list.txt"
    with open(output_file, "w") as f:
        f.write(f"Process List collected at {datetime.now()}\n\n")
        for proc in psutil.process_iter(['pid', 'name', 'username']):
            try:
                f.write(f"PID: {proc.info['pid']} | Name: {proc.info['name']} | User: {proc.info['username']}\n")
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                continue
    print(f"Process list saved to {output_file}")

if __name__ == "__main__":
    collect_processes()
