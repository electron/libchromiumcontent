FROM ubuntu:16.04

ADD . /workspace/libchromiumcontent
ADD s3credentials /config/s3credentials

WORKDIR /workspace/libchromiumcontent

RUN script/docker-install-build-deps.sh
