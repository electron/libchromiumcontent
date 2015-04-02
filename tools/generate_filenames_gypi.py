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

EXCLUDE_SHARED_LIBRARIES = {
  'darwin': [],
  'linux': [
    'ffmpegsumo.so',
  ],
  'win32': [],
}[TARGET_PLATFORM]

GYPI_TEMPLATE = """\
{
  'variables': {
    'libchromiumcontent_dir': '%(src)s',
    'libchromiumcontent_shared_libraries': %(shared_libraries)s,
  },
}
"""


def main(target_file, src):
  shared_libraries = searh_files(src, SHARED_LIBRARY_SUFFIX,
                                 EXCLUDE_SHARED_LIBRARIES)
  content = GYPI_TEMPLATE % {
    'src': os.path.dirname(target_file),
    'shared_libraries': shared_libraries,
  }
  with open(target_file, 'wb+') as f:
    f.write(content)


def searh_files(src, suffix, exclude):
  files = glob.glob(os.path.join(src, '*.' + suffix))
  files = list(set(files) - set(exclude))
  return [os.path.abspath(f) for f in files]


if __name__ == '__main__':
  sys.exit(main(sys.argv[1], sys.argv[2]))
