import os
import subprocess
import sys

from config import TOOLS_DIR


VERSION = '70a3689'
SUPPORTED_PLATFORMS = {
  'cygwin': 'windows',
  'darwin': 'mac',
  'linux2': 'linux',
  'win32': 'windows',
}


def is_platform_supported(platform):
  return platform in SUPPORTED_PLATFORMS


def get_binary_path():
  platform = sys.platform
  if not is_platform_supported(platform):
    return None

  platform_dir = SUPPORTED_PLATFORMS[platform]

  path = os.path.join(TOOLS_DIR, 'sccache', VERSION, platform_dir, 'sccache')
  if platform_dir == 'windows':
    path += '.exe'

  return path


def run(*args):
  binary_path = get_binary_path()
  if binary_path is None:
    raise Exception('No sccache binary found for the current platform.')

  call_args = [binary_path] + list(args)
  return subprocess.call(call_args)
