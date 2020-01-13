#!/usr/bin/python3
import time
import os

# Get variables from Dockerfile or user arguments
server = os.getenv("DNS_SERVER")
refresh = int(os.getenv("REFRESH_INTERVAL"))  # in minutes
cache_size = os.getenv("CACHE_SIZE")  # DNS cache size (0=off)
blacklist = bool(str(os.getenv("BLACKLIST_FILTER")).capitalize())

blacklist_dir = "/blacklists"
whitelist_dir = "/whitelists"
blacklist_hosts = "/blacklist-hosts"


def make_host_lists():
    """ Loads /blacklists and stripes out the ones in /whitelists.
    Writes 0.0.0.0 records for the remaining blacklisted hosts."""

    whitelist = []
    for file in os.listdir(whitelist_dir):
        with open(os.path.join(whitelist_dir, file), "r") as f:
            for line in f.readlines():
                if not line.startswith("#"):
                    if line.endswith("\n"):
                        line = line[:-1]
                    whitelist.append(line)

    for file in os.listdir(blacklist_dir):
        with open(os.path.join(blacklist_dir, file), "r") as src:
            with open(os.path.join(blacklist_hosts, file), "w") as dst:
                for line in src.readlines():
                    if line != "\n":
                        print(1)
                        if line.endswith("\n"):
                            line = line[:-1]
                        if not line.startswith("#"):
                            print(2)
                            if "localhost" not in line:
                                print(3)
                                for host in whitelist:
                                    if host in line:
                                        print("break")
                                        break
                                else:
                                    print(f"writing {line}")
                                    if line.startswith("0.0.0.0 "):
                                        dst.write(f"{line}\n")
                                    else:
                                        dst.write(f"0.0.0.0 {line}\n")


# Set dnsmasq configs appropriately
config = f"""

server={server} # DNS forwarding server
cache-size={cache_size} # DNS cache size (0=off)

"""

if __name__ == '__main__':

    make_host_lists()

    # Add all blacklists
    for file in os.listdir(blacklist_hosts):
        print(f"Adding blacklist: {os.path.join(blacklist_hosts, file)}.")
        config += f"addn-hosts={os.path.join(blacklist_hosts, file)}\n"

    # write to config (and override)
    with open("/etc/dnsmasq.conf", "w") as f:
        f.write(config)

    # "Etrypoint" for container loop
    while True:
        print("{} - Restarting dnsmasq...".format(time.strftime("%d.%m.%Y %H:%M:%S")))
        os.system("service dnsmasq restart")
        time.sleep(60 * refresh)
