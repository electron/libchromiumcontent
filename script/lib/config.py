#!/usr/bin/env python

import os
import platform
import sys

SOURCE_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
SRC_DIR = os.path.join(SOURCE_ROOT, 'src')
TOOLS_DIR = os.path.join(SOURCE_ROOT, 'tools')
VENDOR_DIR = os.path.join(SOURCE_ROOT, 'vendor')
DEPOT_TOOLS_DIR = os.path.join(VENDOR_DIR, 'depot_tools')

COMPONENTS = ['static_library', 'shared_library', 'ffmpeg', 'tests', 'native_mksnapshot']

# URL to the mips64el sysroot image.
MIPS64EL_SYSROOT = 'https://github.com/electron/debian-sysroot-image-creator/releases/download/v0.5.0/debian_jessie_mips64-sysroot.tar.bz2'
# URL to the mips64el toolchain.
MIPS64EL_GCC = 'cross-gcc-4.9.3-n64-loongson-rc5.4'
MIPS64EL_GCC_URL = 'https://github.com/electron/debian-sysroot-image-creator/releases/download/v0.5.0/' + MIPS64EL_GCC + '.tar.gz'

# Whether the host system is an arm64 machine
IS_ARM64_HOST = platform.machine() == 'aarch64'
# Whether the host system is an arm64 machine
IS_ARMV7_HOST = platform.machine() == 'armv7l'

PLATFORM_KEY = {
  'cygwin': 'win',
  'darwin': 'osx',
  'linux2': 'linux',
  'win32': 'win',
}[sys.platform]

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
