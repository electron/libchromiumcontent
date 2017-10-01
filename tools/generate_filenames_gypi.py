#!/usr/bin/env python

import glob
import os
import re
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
    'libwidevinecdm.dylib',
  ],
  'linux': [
    'libwidevinecdm.so',
    'libwidevinecdmadapter.so',
  ],
  'win32': [
    'd3dcompiler_47.dll',
    'libEGL.dll',
    'libGLESv2.dll',
    'widevinecdm.dll',
    'widevinecdmadapter.dll',
  ],
}[TARGET_PLATFORM]
EXCLUDE_STATIC_LIBRARIES = {
  'darwin': [
    'libffmpeg_yasm.a',
    'libppapi_cpp.a',
    'libv8_nosnapshot.a',
  ],
  'linux': [
    'libffmpeg_yasm.a',
    'libppapi_cpp.a',
    'libprotobuf_full_do_not_use.a',
    'libgenperf_libs.a',
    'libv8_nosnapshot.a',
    'libtranslator_static.a',
  ],
  'win32': [
    'ffmpeg.dll.lib',
    'ffmpeg_yasm.lib',
    'libEGL.dll.lib',
    'libGLESv2.dll.lib',
    'ppapi_cpp.lib',
    'widevinecdm.dll.lib',
    'widevinecdmadapter.dll.lib',
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
  (shared_libraries, shared_v8_libraries) = find_libraries(
      shared_dir, SHARED_LIBRARY_SUFFIX, EXCLUDE_SHARED_LIBRARIES)
  (static_libraries, static_v8_libraries) = find_libraries(
      static_dir, STATIC_LIBRARY_SUFFIX, EXCLUDE_STATIC_LIBRARIES)
  content = GYPI_TEMPLATE % {
    'src': repr(os.path.abspath(code_dir)),
    'shared_libraries_dir': repr(os.path.abspath(shared_dir)),
    'static_libraries_dir': repr(os.path.abspath(static_dir)),
    'shared_libraries': shared_libraries,
    'shared_v8_libraries': shared_v8_libraries,
    'static_libraries': static_libraries,
    'static_v8_libraries': static_v8_libraries,
  }
  with open(target_file, 'wb+') as f:
    f.write(content)


def find_libraries(dirpath, library_suffix, list_of_excludes):
  libraries = glob.glob(os.path.join(dirpath, '*.' + library_suffix))
  if (library_suffix == 'so'):
    # Handle "libname.so.123"
    libraries += find_files_by_regex(dirpath, re.compile('.*\.so\.[0-9]+'))

  libraries = [lib
    for lib in libraries
    if os.path.basename(lib) not in list_of_excludes
  ]

  v8_libraries = [lib
    for lib in libraries
    if is_v8_library(lib)
  ]
  other_libraries = [lib
    for lib in libraries
    if lib not in v8_libraries
  ]

  return (
    [os.path.abspath(l) for l in other_libraries],
    [os.path.abspath(l) for l in v8_libraries]
  )


def find_files_by_regex(dirpath, regex):
  files_found = []

  for root, dirs, files in os.walk(dirpath):
    for file in files:
      if regex.match(file):
        files_found.append(os.path.join(root, file))

  return files_found


def is_v8_library(p):
  return (os.path.basename(p).startswith(('v8', 'libv8')) or
          os.path.basename(p).startswith(('icu', 'libicu')))


if __name__ == '__main__':
  sys.exit(main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]))
