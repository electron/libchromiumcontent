#!/usr/bin/env python

import sys


def get_output_dir(target_arch, component):
  # Build in "out_component" for component build.
  output_dir = 'out'
  if component == 'shared_library':
    output_dir += '_component'

  # Build in "out_32" for 32bit target.
  if target_arch == 'ia32':
    output_dir += '_32'
  return output_dir


def get_configuration(config, target_arch):
  if target_arch == 'x64' and sys.platform in ['win32', 'cygwin']:
    config += '_x64'
  return config
