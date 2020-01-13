FROM debian:buster

ENV DNS_SERVER 1.1.1.1
ENV REFRESH_INTERVAL 60
ENV CACHE_SIZE 0

RUN apt-get update -y
RUN apt-get install -y dnsmasq nano net-tools bmon wget htop dnsutils python3

RUN mkdir /blacklists && chmod 777 /blacklists
RUN mkdir /whitelists && chmod 777 /whitelists
RUN mkdir /blacklist-hosts && chmod 777 /blacklist-hosts

ADD run.py /run.py
RUN chmod +x /run.py

CMD "/run.py"
