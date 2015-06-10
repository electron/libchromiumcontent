# libchromiumcontent

A single, shared library that includes the [Chromium Content
module](http://www.chromium.org/developers/content-module) and all its
dependencies (e.g., WebKit, V8, etc.).

## Using it in your app

TODO

## Development

### Prerequisites

* Python 2.7

#### Mac

* Xcode 5.1

#### Windows

* Visual Studio 2013 Professional Update 4

#### Linux

##### CentOS 6.5

`sudo yum install -y pciutils-devel git tar gcc pkg-config atk-devel pulseaudio-libs-devel gdk-devel gdk-pixbuf2-devel gdk-pixbuf2 pygtk2-devel libXtst-devel libXScrnSaver-devel dbus-devel GConf2-devel libgnome-keyring-devel libexif-devel gperf`

##### Ubuntu 14.04

`sudo apt-get install -y build-essential bison libasound2-dev libatk1.0-dev libcups2-dev libexif-dev
 libgconf2-dev libgnome-keyring-dev libgtk2.0-dev libpci-dev libpulse libxtst-dev gperf`

### One-time setup

    $ script/bootstrap

### Building

    $ script/update -t x64
    $ script/build -t x64

### Updating project files

If you change `VERSION` to point to a different Chromium release, or modify
`chromiumcontent.gyp{,i}`, you should run:

    $ script/update

This will regenerate all the project files. Then you can build again.
