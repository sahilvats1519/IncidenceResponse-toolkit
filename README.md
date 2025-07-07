# IncidenceResponse-toolkit
A toolkit for automating and supporting incident response tasks.
## Features

- **Log Collector**: Collects system log timestamps and saves them to `system_logs.txt`.

## How to Use

1. Clone this repository:
git clone https://github.com/sahilvats1519/IncidenceResponse-toolkit.git
2. Navigate to the scripts folder:
cd IncidenceResponse-toolkit/scripts
3. Run the log collector script:
python log_collector.py
4. Check for `system_logs.txt` in the same folder.
Save the README.md file.


## Included Tools

- **log_collector.py**: Collects a simple timestamped log (template for further log collection).
- **process_collector.py**: Lists running processes and saves them to `process_list.txt`.
- **network_info_collector.py**: Saves network interface details and active connections to `network_info.txt`.
- **malware_scanner_stub.py**: Scans a directory for files with known malicious hashes and reports results.

## How to Use

1. **Clone this repository**  
git clone https://github.com/sahilvats1519/IncidenceResponse-toolkit.git
2. **Navigate to the scripts folder**  
cd IncidenceResponse-toolkit/scripts
3. **Run a tool**  
Example:
python process_collector.py

4. **For malware_scanner_stub.py**, enter the path you want to scan when prompted.

## Requirements

- Python 3.x
- psutil (`pip install psutil`)

## Contributing

Pull requests and feature suggestions are welcome!
