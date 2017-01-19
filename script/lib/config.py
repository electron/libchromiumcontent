#!/usr/bin/env python

import os
import sys


def get_output_dir(target_arch, component):
  # Determine the output dir according to target_arch and component.
  if component == 'ffmpeg':
    output_dir = 'ffmpeg'
  elif component == 'shared_library':
    output_dir = 'component'
  elif component == 'static_library':
    output_dir = 'static'

  # Build in "out/component_32" for 32bit target.
  if target_arch == 'ia32':
    output_dir += '_32'
  elif target_arch == 'arm':
    output_dir += '_arm'

  return os.path.join('out', output_dir)


def get_configuration(target_arch):
  config = 'Release'
  if target_arch == 'x64' and sys.platform in ['win32', 'cygwin']:
    config += '_x64'
  return config
