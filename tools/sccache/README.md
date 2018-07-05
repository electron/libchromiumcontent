## sccache

Shared Compilation Cache  
https://github.com/mozilla/sccache

### Building a portable binary version on Mac

The goal is to build a binary that would not require `openssl` to be installed in the system. The project's docs provide [build instructions](https://github.com/mozilla/sccache#building-portable-binaries)  for that but they're quite laconic.

1. Install `rust` version `[1.22.0, 1.25.0)`, `1.22.1` works well. See [mozilla/sccache#233](https://github.com/mozilla/sccache/issues/233) for the explanation of the versions range.  
Old versions might not be available via [Homebrew](https://brew.sh) but `brew install https://raw.githubusercontent.com/Homebrew/homebrew-core/2b57a70c4bb1ac9bec3e6de1beda98f5dafcdf7c/Formula/rust.rb` should work (it will install `rust@1.22.1`).
2. Clone the repo:  
`git clone https://github.com/marshallofsound/sccache.git`
3. `cd sccache`
4. Checkout version 70a36893769ffba0202f831cb3582881f90ca790:  
`git fetch --tags && git checkout 70a36893769ffba0202f831cb3582881f90ca790`
5. `export OPENSSL_STATIC=yes`
6. Build the project in a release mode:  
`cargo build --release`.
7. Resulting `sccache` binary will appear in the `./target/release/`.
