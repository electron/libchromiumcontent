FROM ubuntu:16.04

RUN apt-get update && apt-get install -y --force-yes \
  bison \
  build-essential \
  curl \
  clang \
  g++-5-arm-linux-gnueabihf \
  g++-arm-linux-gnueabihf \
  gcc-5-arm-linux-gnueabihf \
  gcc-arm-linux-gnueabihf \
  git \
  gperf \
  libasound2-dev \
  libc6-dev-armhf-cross \
  libcap-dev \
  libcups2-dev \
  libdbus-1-dev \
  libgconf2-dev \
  libgnome-keyring-dev \
  libgtk2.0-dev \
  libnotify-dev \
  libnss3-dev \
  libxss1 \
  libxtst-dev \
  linux-libc-dev-armhf-cross \
  nodejs \
  python

ADD . /workspace/libchromiumcontent
ADD s3credentials /config/s3credentials

WORKDIR /workspace/libchromiumcontent
