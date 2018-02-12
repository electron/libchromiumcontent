#!/usr/bin/env python

import os
import platform

SOURCE_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
VENDOR_DIR = os.path.join(SOURCE_ROOT, 'vendor')

# URL to the mips64el sysroot image.
MIPS64EL_SYSROOT = 'https://github.com/electron/debian-sysroot-image-creator/releases/download/v0.5.0/debian_jessie_mips64-sysroot.tar.bz2'
# URL to the mips64el toolchain.
MIPS64EL_GCC = 'cross-gcc-4.9.3-n64-loongson-rc5.4'
MIPS64EL_GCC_URL = 'https://github.com/electron/debian-sysroot-image-creator/releases/download/v0.5.0/' + MIPS64EL_GCC + '.tar.gz'


def set_mips64el_env(env):
  gcc_dir = os.path.join(VENDOR_DIR, MIPS64EL_GCC)
  ldlib_dirs = [
    gcc_dir + '/usr/x86_64-unknown-linux-gnu/mips64el-loongson-linux/lib',
    gcc_dir + '/usr/lib64',
    gcc_dir + '/usr/mips64el-loongson-linux/lib64',
    gcc_dir + '/usr/mips64el-loongson-linux/sysroot/lib64',
    gcc_dir + '/usr/mips64el-loongson-linux/sysroot/usr/lib64',
  ]
  env['LD_LIBRARY_PATH'] = os.pathsep.join(ldlib_dirs)
  env['PATH'] = os.pathsep.join([gcc_dir + '/usr/bin', env['PATH']])


def get_output_dir(source_root, target_arch, component):
  return os.path.join(source_root, 'src', 'out-' + target_arch, component)
