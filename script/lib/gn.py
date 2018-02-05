import os
import subprocess
import sys


def __get_executable_path(chromium_root_dir):
  platform = sys.platform
  relative_path = None

  if platform in ['win32', 'cygwin']:
    relative_path = ['buildtools', 'win', 'gn.exe']
  elif platform == 'linux2':
    relative_path = ['buildtools', 'linux64', 'gn']
  elif platform == 'darwin':
    relative_path = ['buildtools', 'mac', 'gn']

  assert relative_path is not None, "Platform '{}' is not supported".format(platform)

  absolute_path = os.path.join(chromium_root_dir, *relative_path)
  return absolute_path


def create_args(out_dir, raw_config, **kwargs):
  named_arguments = ['{0} = "{1}"\n'.format(k, v) for k, v in kwargs.iteritems()]

  with open(os.path.join(out_dir, 'args.gn'), 'w') as f:
    lines_to_write = named_arguments + ['#' * 80 + '\n']
    f.writelines(lines_to_write)
    f.write(raw_config)


def generate(out_dir, chromium_root_dir, env):
  executable = __get_executable_path(chromium_root_dir)
  out_dir_relative_path = os.path.relpath(out_dir, chromium_root_dir)
  subprocess.check_call([executable, 'gen', out_dir_relative_path],
                        cwd=chromium_root_dir, env=env)
