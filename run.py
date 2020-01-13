#!/usr/bin/python3
import time
import os

# Get variables from Dockerfile or user arguments
server = os.getenv("DNS_SERVER")
refresh = int(os.getenv("REFRESH_INTERVAL")) # in minutes
cache_size = os.getenv("CACHE_SIZE") # DNS cache size (0=off)

# Set dnsmasq configs appropriately
config = f"""

server={server} # DNS forwarding server
cache-size={cache_size} # DNS cache size (0=off)

"""

# write to config (and override)
with open("/etc/dnsmasq.conf","w") as f:
    f.write(config)


# "Etrypoint" for container loop
while True:
    print("{} - Restarting dnsmasq...".format(time.strftime("%d.%m.%Y %H:%M:%S")))
    os.system("service dnsmasq restart")
    time.sleep(60*refresh)
