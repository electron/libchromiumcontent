FROM ubuntu:16.04

ADD . /workspace/libchromiumcontent
ADD s3credentials /config/s3credentials

WORKDIR /workspace/libchromiumcontent

RUN apt-get update && apt-get -y --force-yes install lsb-release
RUN script/docker-install-build-deps.sh --syms --no-prompt
