#!/usr/bin/env python

import sys


def get_output_dir(target_arch, component):
  # Build in "out/ffmpeg" for Chromium branding of ffmpeg.
  if component == 'ffmpeg':
    return 'ffmpeg'

  # Build in "out/component" for component build.
  if component == 'shared_library':
    output_dir = 'component'
  else:
    output_dir = 'static'

  # Build in "out/component_32" for 32bit target.
  if target_arch == 'ia32':
    output_dir += '_32'
  elif target_arch == 'arm':
    output_dir += '_arm'

  return output_dir


def get_configuration(target_arch):
  config = 'Release'
  if target_arch == 'x64' and sys.platform in ['win32', 'cygwin']:
    config += '_x64'
  return config
