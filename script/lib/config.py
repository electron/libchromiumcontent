#!/usr/bin/env python

import os


def get_output_dir(source_root, target_arch, component):
  return os.path.join(source_root, 'out-' + target_arch, component)
