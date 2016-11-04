# libchromiumcontent

Automatially builds and provides prebuilt binaries of [Chromium Content
module](http://www.chromium.org/developers/content-module) and all its
dependencies (e.g., Blink, V8, etc.).

## Development

### Prerequisites

* [Linux](https://chromium.googlesource.com/chromium/src/+/master/docs/linux_build_instructions_prerequisites.md)
* [Mac](https://chromium.googlesource.com/chromium/src/+/master/docs/mac_build_instructions.md#Prerequisites)
* [Windows](https://chromium.googlesource.com/chromium/src/+/master/docs/windows_build_instructions.md)

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

### Building for ARM target

```bash
$ ./script/bootstrap
$ ./script/update -t arm
$ cd vendor/chromium/src
$ ./build/install-build-deps.sh --arm
$ ./chrome/installer/linux/sysroot_scripts/install-debian.wheezy.sysroot.py --arch=arm
$ cd -
$ ./script/build -t arm
```
