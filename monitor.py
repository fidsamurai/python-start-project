#!/usr/bin/env python3
#Module psutil needs to be installed via pip3 first.
#Python script to Monitor Server Resources.

import time
import psutil
import smtplib

cpu_thresh = 50.0
cpu_pct = psutil.cpu_percent(interval=1)

if cpu_pct >= cpu_thresh:
    cpu_alert = "CPU Warning, CPU at ",cpu_pct, "percent"
else:
    cpu_alert = ""

mem = psutil.virtual_memory()
mem_thresh = 1024 * 1024 * 1024 #change the end value to choose the amount of MB

if mem_thresh >= mem.available:
    mem_alert = "Memory Usage Warning only", round((mem.available /1024 /1024), 2), "MB available"
else:
    mem_alert = ""
partition1 = '/'
disk1 = psutil.disk_usage(partition1)
disk_thresh = 85.0

if disk_thresh <= disk1[3]:
    disk_alert = print("Root volume usage warning", disk1[3], "% used")
else:
    disk_alert = ""

def net_usage(inf = "eth0"):   #change the inf variable according to the interface
  global net_in_alert
  global net_out_alert
  net_in_ps1 = psutil.net_io_counters(pernic=True, nowrap=True)[inf]
  net_in_1 = net_in_ps1.bytes_recv
  net_out_1 = net_in_ps1.bytes_sent
  time.sleep(1)
  net_in_ps2 = psutil.net_io_counters(pernic=True, nowrap=True)[inf]
  net_in_2 = net_in_ps2.bytes_recv
  net_out_2 = net_in_ps2.bytes_sent
  net_in_res = round((net_in_2 - net_in_1) /1024 /1024, 2)
  net_out_res = round((net_out_2 - net_out_1) /1024 /1024, 2)
  net_in_thresh = 1.5
  net_out_thresh = 1.5
  if net_in_res <= net_in_thresh:
      net_in_alert = f"Current net-usage:IN:", net_in_res, "MB/s"
  else:
      net_in_alert = ""
  if net_out_res <= net_out_thresh:
     net_out_alert = f"Current net-usage:OUT:", net_out_res, "MB/s"
  else:
      net_out_alert = "" 
net_usage()

message_list = []

if cpu_alert == "":
    pass
else:
    message_list.append(cpu_alert)
if mem_alert == "":
    pass
else:
    message_list.append(mem_alert)
if disk_alert == "":
    pass
else:
    message_list.append(disk_alert)
if net_in_alert == "":
    pass
else:
    message_list.append(net_in_alert)
if net_out_alert == "":
    pass
else:
    message_list.append(net_out_alert)

print(str(message_list))
if message_list == "":
  pass
else:
  def alerts():
    sender = 'faga@linuxlab.org'
    receivers = ['faga@linuxlab.org']
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(sender, "redhat237")
    server.sendmail(sender, receivers, str(message_list))
alerts()
