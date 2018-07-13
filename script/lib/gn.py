import os
import subprocess
import sys


def __get_executable_path(depot_tools_dir):
  gn_path = os.path.join(depot_tools_dir, 'gn')
  if sys.platform in ['win32', 'cygwin']:
    gn_path += '.bat'

  return gn_path


def create_args(out_dir, raw_config, **kwargs):
  named_arguments = ['{0} = "{1}"\n'.format(k, v) for k, v in kwargs.iteritems()]

  if not os.path.isdir(out_dir):
    os.makedirs(out_dir)

  with open(os.path.join(out_dir, 'args.gn'), 'w') as f:
    lines_to_write = named_arguments + ['#' * 80 + '\n']
    f.writelines(lines_to_write)
    f.write(raw_config)


def generate(out_dir, chromium_root_dir, depot_tools_dir, env, verbose):
  executable = __get_executable_path(depot_tools_dir)
  out_dir_relative_path = os.path.relpath(out_dir, chromium_root_dir)
  gn_args = [executable, 'gen', out_dir_relative_path]
  if verbose:
    gn_args.append('-v')
  subprocess.check_call(gn_args, cwd=chromium_root_dir, env=env)
