FROM jenkins/jenkins:lts-jdk11
USER root
WORKDIR /usr/src/app

RUN apt-get update  \
    && apt-get -y install wget  \
    && apt-get -y install zip  \
    && apt-get -y install unzip \
    && apt-get install -y python3 \
    && apt-get -y install nano  \
    && apt-get -y install libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \

USER jenkins
