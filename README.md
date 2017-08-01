# libchromiumcontent

Automatically builds and provides prebuilt binaries of the [Chromium Content
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

If you switch to a different Chromium release, or modify
files inside the `chromiumcontent` directory, you should run:

    $ script/update

This will regenerate all the project files. Then you can build again.

### Building for ARM target

> TODO: This section may be out of date, needs review

```bash
$ ./script/bootstrap
$ ./script/update -t arm
$ cd vendor/chromium/src
$ ./build/install-build-deps.sh --arm
$ ./chrome/installer/linux/sysroot_scripts/install-debian.wheezy.sysroot.py --arch=arm
$ cd -
$ ./script/build -t arm
```


### Building for ARM64 target

```bash
$ ./script/bootstrap
$ ./script/update -t arm64
$ ./script/build -t arm64
$ ./script/create-dist -t arm64
```

## Releases

There is no formal release process for libchromiumcontent, as release artifacts
are created as a byproduct of CI. When a build is successful, its compiled
asset is automatically uploaded to S3. These assets are later downloaded as 
part of Electron's bootstrap script.  These files are about 4GB, so the 
bootstrap task takes a while to run.

Asset URLs have the following format:

```js
`https://s3.amazonaws.com/github-janky-artifacts/libchromiumcontent/${platform}/${commit}/libchromiumcontent.zip`
```

Builds exist for the following platform/arch pairs:

- `osx/x64`
- `mas/x64`
- `win/ia32`
- `win/x64`
- `linux/ia32`
- `linux/x64`
- `linux/ar`

The Linux machines only build for pushes by GitHub employees, so PRs 
from third parties have to have their linux builds triggered manually.

Each platform/arch has its own CI task, so it should be made sure that all 
platform/arch have the CI tasks started and finished. To verify that
a given commit has all the necessary build artifacts:

```
npm i -g electron/libcc-check
libcc-check 7a9d4a1c9c265468dd54005f6c1920b2cc2c8ec3
```

## Setting libchromiumcontent version in Electron

For Electron versions 1.7 and higher, libchromiumcontent is vendored as a git 
submodule in the Electron repo. To change the version that Electron is using,
use git to check out the target branch / SHA:

```
cd electron/electron/vendor/libchromiumcontent
git checkout some-branch-or-sha
```

For Electron versions 1.6 and lower, libchromiumcontent is vendored as part
of a (now retired) project called brightray. To change the version that 
Electron is using, change the commit SHA in [config.py](https://github.com/electron/electron/blob/0428632a4e5dfa65e7ffbe39ff208069f0b9cdc4/script/lib/config.py#L12).