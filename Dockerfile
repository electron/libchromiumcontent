FROM ubuntu:16.04

# Set up TEMP directory
ENV TEMP=/tmp
RUN chmod a+rwx /tmp

# Set up HOME directory
ENV HOME=/home
RUN chmod a+rwx /home

# Install Linux packages
ADD script/docker-install-build-deps.sh /setup/install-build-deps.sh
RUN apt-get update && apt-get -y --force-yes install lsb-release locales
RUN /setup/install-build-deps.sh --syms --no-prompt --no-chromeos-fonts
