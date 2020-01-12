# easy-dnsmasq
<img alt="Docker Cloud Automated build" src="https://img.shields.io/docker/cloud/automated/theclocktwister/easy-dnsmasq"> <img alt="Docker Pulls" src="https://img.shields.io/docker/pulls/theclocktwister/easy-dnsmasq"> <img alt="Docker Cloud Build Status" src="https://img.shields.io/docker/cloud/build/theclocktwister/easy-dnsmasq"> <img alt="GitHub code size in bytes" src="https://img.shields.io/github/languages/code-size/TheClockTwister/easy-dnsmasq"> <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/TheClockTwister/easy-dnsmasq">

This docker image is meant to supply a minimalistic and flexible DNS-forwarding service using [dnsmasq](https://wiki.ubuntuusers.de/Dnsmasq/).

<img src="https://raw.githubusercontent.com/TheClockTwister/easy-dnsmasq/master/schematic.png">


## Features
- Allows host entries for the whole network
- Easy to handle (like /etc/hosts or C:\Windows\System32\drivers\etc\hosts)
- Allows multiple failover DNS server
- DNS caching override (on/off)
- Custon DNS cache size



## Deployment
To deploy the DNS server on your host, you can copy the following compose file:
```yaml
version: '3.3'
services:
  own-dnsmasq:
    image: theclocktwister/easy-dnsmasq:latest
    ports:
      - 53:53/udp
    environment:
      DNS_SERVER: 1.1.1.1 # Chosse your primary DNS server
      REFRESH_INTERVAL: 60 # The interval ro reload the /etc/hosts file and restart dnsmasq
    volumes:
      - /Services/DNS/hosts.conf:/etc/hosts # static hosts look-up table
    restart: always
    cap_add:
      - NET_ADMIN # needed for network stack access
```

### Environment variables
You can specify certain values by using the `-e`option in docker run, or the `environment` section in docker-compose files. The following variables are recognized:

- `DNS_SERVER` This is the DNS server to forward unknown queries to (default: 1.1.1.1)
- `REFRESH_INTERVAL` The interval (in minutes) in which the /etc/hosts config is reloaded and dnsmasq restarted (default: 60)
