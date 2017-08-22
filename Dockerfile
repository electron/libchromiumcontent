FROM ubuntu:16.04

RUN groupadd --gid 1000 builduser \
  && useradd --uid 1000 --gid builduser --shell /bin/bash --create-home builduser

# Set up TEMP directory
ENV TEMP=/tmp
RUN chmod a+rwx /tmp

# Install Linux packages
ADD script/docker-install-build-deps.sh /setup/install-build-deps.sh
RUN apt-get update && apt-get -y --force-yes install lsb-release locales
RUN /setup/install-build-deps.sh --syms --no-prompt --no-chromeos-fonts

RUN apt-get install -y python-setuptools
RUN easy_install -U pip
RUN pip install -U crcmod

RUN mkdir /tmp/workspace
RUN chown builduser:builduser /tmp/workspace

USER builduser
WORKDIR /home/builduser

# Prime the LIBCHROMIUMCONTENT_GIT_CACHE and src dirs
RUN mkdir /tmp/libcc_cache
RUN chown builduser:builduser /tmp/libcc_cache
RUN git clone https://github.com/electron/libchromiumcontent.git project
WORKDIR /home/builduser/project
RUN git checkout circleci_test
RUN script/bootstrap
RUN export LIBCHROMIUMCONTENT_GIT_CACHE=/tmp/libcc_cache
RUN script/update --source_only

WORKDIR /home/builduser
