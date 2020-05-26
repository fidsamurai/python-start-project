#!/usr/bin/env python3
#Module psutil needs to be installed via pip3 first.
#Python script to Monitor Server Resources.

import time
import psutil

cpu_thresh = 50.0
cpu_pct = psutil.cpu_percent(interval=1)

if cpu_pct >= cpu_thresh:
    print("CPU Warning, CPU at ",cpu_pct, "percent")

mem = psutil.virtual_memory()
mem_thresh = 1024 * 1024 * 1024 #change the end value to choose the amount of MB

if mem_thresh >= mem.available:
    print("Memory Usage Warning only", round((mem.available /1024 /1024), 2), "MB available")

partition1 = '/'
disk1 = psutil.disk_usage(partition1)
disk_thresh = 85.0

if disk_thresh <= disk1[3]:
    print("Root volume usage warning", disk1[3], "% used")

def net_usage(inf = "eth0"):   #change the inf variable according to the interface
  net_in_ps1 = psutil.net_io_counters(pernic=True, nowrap=True)[inf]
  net_in_1 = net_in_ps1.bytes_recv
  net_out_1 = net_in_ps1.bytes_sent
  time.sleep(1)
  net_in_ps2 = psutil.net_io_counters(pernic=True, nowrap=True)[inf]
  net_in_2 = net_in_ps2.bytes_recv
  net_out_2 = net_in_ps2.bytes_sent
  net_in_res = round((net_in_2 - net_in_1) /1024 /1024, 3)
  net_out_res = round((net_out_2 - net_out_1) /1024 /1024, 3)
  print(f"Current net-usage:\nIN: {net_in_res} MB/s, OUT: {net_out_res} MB/s")
  net_in_thresh = 1.5
  net_out_thresh = 1.5
  if net_in_res <= net_in_thresh:
     print(f"Current net-usage:\nIN: {net_in_res} MB/s")
  if net_out_res <= net_out_thresh:
     print(f"Current net-usage:\nOUT: {net_out_res} MB/s")

net_usage()
