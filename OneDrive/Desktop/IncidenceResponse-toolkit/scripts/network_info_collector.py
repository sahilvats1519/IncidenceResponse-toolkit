# scripts/network_info_collector.py

import psutil
from datetime import datetime

def collect_network_info():
    output_file = "network_info.txt"
    with open(output_file, "w") as f:
        f.write(f"Network Info collected at {datetime.now()}\n\n")
        
        # Network interfaces and IPs
        f.write("Network Interfaces and IP Addresses:\n")
        addrs = psutil.net_if_addrs()
        for interface, addr_list in addrs.items():
            f.write(f"{interface}:\n")
            for addr in addr_list:
                f.write(f"  {addr.family}: {addr.address}\n")
        f.write("\n")
        
        # Network connections
        f.write("Active Network Connections:\n")
        for conn in psutil.net_connections():
            try:
                laddr = f"{conn.laddr.ip}:{conn.laddr.port}" if conn.laddr else ""
                raddr = f"{conn.raddr.ip}:{conn.raddr.port}" if conn.raddr else ""
                f.write(f"{conn.type} {laddr} -> {raddr} Status: {conn.status}\n")
            except Exception:
                continue
    print(f"Network info saved to {output_file}")

if __name__ == "__main__":
    collect_network_info()
