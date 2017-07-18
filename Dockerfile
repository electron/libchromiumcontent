FROM ubuntu:16.04

ENV TEMP=/tmp
RUN chmod a+rwx /tmp

ADD script/docker-install-build-deps.sh /setup/install-build-deps.sh

RUN apt-get update && apt-get -y --force-yes install lsb-release locales
RUN /setup/install-build-deps.sh --syms --no-prompt --no-chromeos-fonts
