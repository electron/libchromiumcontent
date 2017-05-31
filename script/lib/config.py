#!/usr/bin/env python

import os


def get_output_dir(source_root, target_arch, component):
  return os.path.join(source_root, 'vendor', 'chromium', 'src', 'out-' + target_arch, component)
