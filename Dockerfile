FROM debian:buster

ENV DNS_SERVER 1.1.1.1
ENV REFRESH_INTERVAL 60

RUN apt-get update -y
RUN apt-get install -y dnsmasq nano net-tools bmon htop dnsutils python3

ADD run.py /run.py
RUN chmod +x /run.py

CMD "/run.py"
