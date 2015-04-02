#!/usr/bin/env python

import glob
import os
import sys


GYPI_TEMPLATE = """\
{
  'variables': {
    'libchromiumcontent_dir': '%(src)s',
    'libchromiumcontent_shared_libraries': %(shared_libraries)s,
  },
}
"""


def main(target_file, src):
  shared_libraries = glob.glob(os.path.join(src, '*.dylib'))
  shared_libraries = [os.path.abspath(l) for l in shared_libraries]
  content = GYPI_TEMPLATE % {
    'src': os.path.dirname(target_file),
    'shared_libraries': shared_libraries,
  }
  with open(target_file, 'wb+') as f:
    f.write(content)


if __name__ == '__main__':
  sys.exit(main(sys.argv[1], sys.argv[2]))
