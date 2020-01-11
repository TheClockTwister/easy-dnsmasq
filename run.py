#!/usr/bin/python3
import time
import os

server = os.getenv("dns_server")
os.system("echo server={} > /etc/dnsmasq.conf".format(server))

while True:
   os.system("service dnsmasq restart")
   print("reload")
   time.sleep(60*60) #restart every hour
