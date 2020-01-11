FROM debian:buster

ENV dns_server 1.1.1.1

RUN apt-get update -y
RUN apt-get install -y dnsmasq nano net-tools bmon htop dnsutils python3

ADD run.py /run.py
RUN chmod +x /run.py

CMD "/run.py"
