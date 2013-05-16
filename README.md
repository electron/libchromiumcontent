# libchromiumcontent

A single, shared library that includes the [Chromium Content
module](http://www.chromium.org/developers/content-module) and all its
dependencies (e.g., WebKit, V8, etc.).

## Using it in your app

TODO

## Development

### Prerequisites

* Python 2.7

### One-time setup

    $ script/bootstrap

### Building

    $ script/build

### Updating project files

If you change `VERSION` to point to a different Chromium revision, or modify
`chromiumcontent.gyp{,i}`, you should run:

    $ script/update

This will regenerate all the project files. Then you can build again.
