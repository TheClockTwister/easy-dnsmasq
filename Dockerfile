FROM debian:buster

ENV DNS_SERVER 1.1.1.1
ENV REFRESH_INTERVAL 60
ENV CACHE_SIZE 0

RUN apt-get update -y
RUN apt-get install -y dnsmasq nano net-tools bmon wget htop dnsutils python3

ADD blacklists /blacklists
RUN mkdir /whitelists && chmod 777 /whitelists

ADD run.py /run.py
RUN chmod +x /run.py

CMD "/run.py"
