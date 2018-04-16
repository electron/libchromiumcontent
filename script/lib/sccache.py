import os
import sys

from config import TOOLS_DIR


VERSION = '0.2.6'
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
