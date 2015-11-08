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
  'darwin': [
  ],
  'linux': [
  ],
  'win32': [
    'd3dcompiler_47.dll',
    'libEGL.dll',
    'libGLESv2.dll',
  ],
}[TARGET_PLATFORM]
EXCLUDE_STATIC_LIBRARIES = {
  'darwin': [
    'libv8_nosnapshot.a',
  ],
  'linux': [
    'libprotobuf_full_do_not_use.a',
    'libgenperf_libs.a',
    'libv8_nosnapshot.a',
  ],
  'win32': [
    'libEGL.dll.lib',
    'libGLESv2.dll.lib',
  ],
}[TARGET_PLATFORM]

GYPI_TEMPLATE = """\
{
  'variables': {
    'libchromiumcontent_src_dir': %(src)s,
    'libchromiumcontent_shared_libraries_dir': %(shared_libraries_dir)s,
    'libchromiumcontent_static_libraries_dir': %(static_libraries_dir)s,
    'libchromiumcontent_shared_libraries': %(shared_libraries)s,
    'libchromiumcontent_shared_v8_libraries': %(shared_v8_libraries)s,
    'libchromiumcontent_static_libraries': %(static_libraries)s,
    'libchromiumcontent_static_v8_libraries': %(static_v8_libraries)s,
  },
}
"""


def main(target_file, code_dir, shared_dir, static_dir):
  (shared_libraries, shared_v8_libraries) = searh_files(
      shared_dir, SHARED_LIBRARY_SUFFIX, EXCLUDE_SHARED_LIBRARIES)
  (static_libraries, static_v8_libraries) = searh_files(
      static_dir, STATIC_LIBRARY_SUFFIX, EXCLUDE_STATIC_LIBRARIES)
  content = GYPI_TEMPLATE % {
    'src': repr(os.path.abspath(os.path.dirname(code_dir))),
    'shared_libraries_dir': repr(os.path.abspath(os.path.dirname(shared_dir))),
    'static_libraries_dir': repr(os.path.abspath(os.path.dirname(static_dir))),
    'shared_libraries': shared_libraries,
    'shared_v8_libraries': shared_v8_libraries,
    'static_libraries': static_libraries,
    'static_v8_libraries': static_v8_libraries,
  }
  with open(target_file, 'wb+') as f:
    f.write(content)

def searh_files(src, suffix, exclude):
  files = glob.glob(os.path.join(src, '*.' + suffix))
  files = [f for f in files if os.path.basename(f) not in exclude]
  return ([os.path.abspath(f) for f in files if not is_v8_library(f)],
          [os.path.abspath(f) for f in files if is_v8_library(f)])


def is_v8_library(p):
  return (os.path.basename(p).startswith(('v8', 'libv8')) or
          os.path.basename(p).startswith(('icu', 'libicu')))


if __name__ == '__main__':
  sys.exit(main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]))
