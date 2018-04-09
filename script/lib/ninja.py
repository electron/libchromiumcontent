import os
import subprocess
import sys

from lib.config import DEPOT_TOOLS_DIR


def __get_binary_path():
  path = os.path.join(DEPOT_TOOLS_DIR, 'ninja')

  if sys.platform == 'win32':
    path = '{0}.exe'.format(path)

  return path


def run(directory, target=None, env=None):
  ninja_binary = __get_binary_path()

  args = [ninja_binary,
          '-C', directory
         ]
  if target is not None:
    args.append(target)

  subprocess.check_call(args, env=env)
