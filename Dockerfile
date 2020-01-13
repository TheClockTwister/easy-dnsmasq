FROM debian:buster

ENV DNS_SERVER 1.1.1.1
ENV REFRESH_INTERVAL 60
ENV CACHE_SIZE 0

RUN apt-get update -y
RUN apt-get install -y dnsmasq nano net-tools bmon wget htop dnsutils python3

RUN mkdir /blacklists
RUN chmod 777 /blacklists

RUN cd /blacklists
RUN wget https://raw.githubusercontent.com/crazy-max/WindowsSpyBlocker/master/data/hosts/extra.txt
RUN wget https://raw.githubusercontent.com/crazy-max/WindowsSpyBlocker/master/data/hosts/spy.txt
RUN wget https://raw.githubusercontent.com/crazy-max/WindowsSpyBlocker/master/data/hosts/update.txt

ADD run.py /run.py
RUN chmod +x /run.py

CMD "/run.py"
