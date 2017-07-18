FROM ubuntu:16.04

RUN apt-get update && apt-get -y --force-yes install lsb-release locales
RUN script/docker-install-build-deps.sh --syms --no-prompt --no-chromeos-fonts
