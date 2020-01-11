#!/usr/bin/python3
import time
import os

# Get variables from Dockerfile or user arguments
server = os.getenv("DNS_SERVER")
refresh = os.getenv("REFRESH_INTERVAL") # in minutes

# Set dnsmasq configs appropriately
os.system("echo server={} > /etc/dnsmasq.conf".format(server)) # dnsmasq.conf flushed, only forward server


# "Etrypoint" for container loop
while True:
    print("{} - Restarting dnsmasq...".format(time.strftime("%d.%m.%Y %H:%M:%S")))
    os.system("service dnsmasq restart")
    time.sleep(60*refresh)
