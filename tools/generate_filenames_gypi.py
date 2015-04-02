#!/usr/bin/env python

import glob
import os
import sys


TARGET_PLATFORM = {
  'cygwin': 'win32',
  'darwin': 'darwin',
  'linux2': 'linux',
  'win32': 'win32',
}[sys.platform]

SHARED_LIBRARY_SUFFIX = {
  'darwin': 'dylib',
  'linux': 'so',
  'win32': 'dll',
}[TARGET_PLATFORM]
STATIC_LIBRARY_SUFFIX = {
  'darwin': 'a',
  'linux': 'a',
  'win32': 'lib',
}[TARGET_PLATFORM]

EXCLUDE_SHARED_LIBRARIES = {
  'darwin': [],
  'linux': [
    'ffmpegsumo.so',
  ],
  'win32': [],
}[TARGET_PLATFORM]
EXCLUDE_STATIC_LIBRARIES = {
  'darwin': [],
  'linux': [],
  'win32': [],
}[TARGET_PLATFORM]

GYPI_TEMPLATE = """\
{
  'variables': {
    'libchromiumcontent_root_dir': '%(src)s',
    'libchromiumcontent_shared_libraries': %(shared_libraries)s,
    'libchromiumcontent_static_libraries': %(static_libraries)s,
  },
}
"""


def main(target_file, shared_src, static_src):
  shared_libraries = searh_files(shared_src, SHARED_LIBRARY_SUFFIX,
                                 EXCLUDE_SHARED_LIBRARIES)
  static_libraries = searh_files(static_src, STATIC_LIBRARY_SUFFIX,
                                 EXCLUDE_STATIC_LIBRARIES)
  content = GYPI_TEMPLATE % {
    'src': os.path.dirname(target_file),
    'shared_libraries': shared_libraries,
    'static_libraries': static_libraries,
  }
  with open(target_file, 'wb+') as f:
    f.write(content)


def searh_files(src, suffix, exclude):
  files = glob.glob(os.path.join(src, '*.' + suffix))
  files = list(set(files) - set(exclude))
  return [os.path.abspath(f) for f in files]


if __name__ == '__main__':
  sys.exit(main(sys.argv[1], sys.argv[2], sys.argv[3]))
