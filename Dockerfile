FROM ubuntu:16.04

RUN groupadd --gid 1000 builduser \
  && useradd --uid 1000 --gid builduser --shell /bin/bash --create-home builduser

# Set up TEMP directory
ENV TEMP=/tmp
RUN chmod a+rwx /tmp

# Install Linux packages
ADD script/docker-install-build-deps.sh /setup/install-build-deps.sh
RUN apt-get update && apt-get -y --force-yes install lsb-release locales wget
RUN /setup/install-build-deps.sh --syms --no-prompt --no-chromeos-fonts

RUN apt-get install -y python-setuptools
RUN easy_install -U pip
RUN pip install -U crcmod
RUN pip install filechunkio

RUN mkdir /tmp/workspace
RUN chown builduser:builduser /tmp/workspace

USER builduser
WORKDIR /home/builduser
