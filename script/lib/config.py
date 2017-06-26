#!/usr/bin/env python

import os


def get_output_dir(source_root, target_arch, component):
  with open(os.path.join(source_root, 'VERSION')) as f:
    chromium_version = f.readline().strip()

  return os.path.join(source_root, 'src', 'out-' + target_arch,
                      chromium_version, component)
