FROM python:2.7.12

USER root

RUN curl -L -O https://download.elastic.co/beats/filebeat/filebeat_1.3.1_amd64.deb
RUN dpkg -i filebeat_1.3.1_amd64.deb

ADD . /opt/app

WORKDIR /opt/app

RUN cp filebeat.yml /etc/filebeat/filebeat.yml

VOLUME /opt/app

CMD ["bash", "run.sh"]

