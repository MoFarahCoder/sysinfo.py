#!/usr/bin/env python3
"""
sysinfo.py
Prints CPU, memory, and disk usage using psutil if available,
otherwise falls back to Python's standard library.
"""

import shutil, platform, os, sys

try:
    import psutil
except ImportError:
    psutil = None

def bytes_to_gb(b):  # helper
    return b / (1024 ** 3)

def main():
    print(f"System: {platform.system()} {platform.release()}  ({platform.machine()})\n")

    # CPU
    if psutil:
        cpu_count = psutil.cpu_count(logical=True)
        cpu_usage = psutil.cpu_percent(interval=1)
    else:
        cpu_count = os.cpu_count()
        cpu_usage = "n/a"
    print(f"CPU cores : {cpu_count}")
    print(f"CPU usage : {cpu_usage}%\n")

    # Memory
    if psutil:
        mem = psutil.virtual_memory()
        print(f"Memory total : {bytes_to_gb(mem.total):.2f} GB")
        print(f"Memory used  : {bytes_to_gb(mem.used):.2f} GB ({mem.percent}%)\n")
    else:
        print("Memory info  : psutil not installed\n")

    # Disk
    disk = shutil.disk_usage("/")
    used_gb = bytes_to_gb(disk.used)
    total_gb = bytes_to_gb(disk.total)
    percent = (disk.used / disk.total) * 100
    print(f"Disk / total : {total_gb:.2f} GB")
    print(f"Disk / used  : {used_gb:.2f} GB ({percent:.1f}%)")

if __name__ == "__main__":
    main()
