#!/usr/bin/env python3.7
#Module psutil needs to be installed via pip3 first.
#Python script to Monitor Server Resources.

import psutil

cpu_thresh = 50.0
cpu_pct = psutil.cpu_percent(interval=1)

if cpu_pct >= cpu_thresh:
    print("CPU Warning, CPU at ",cpu_pct, "percent")

mem = psutil.virtual_memory()
mem_thresh = 1024 * 1024 * 1024 #500MB

if mem_thresh >= mem.available:
    print("Memory Usage Warning only", mem.available /1024 /1024, "MB available")

partition1 = '/'
disk1 = psutil.disk_usage(partition1)
disk_thresh = 85.0

if disk_thresh <= disk1[3]:
    print("Root volume usage warning", disk1[3], "% used")
