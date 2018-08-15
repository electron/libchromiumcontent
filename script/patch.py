#!/usr/bin/env python
"""
Usage: patch -h

Use this script to selectively apply and reverse patches.
It is mostly useful to fix patches during upgrades to a new Chromium version.
"""

import argparse
import os
import subprocess
import sys

from lib.patches import Patch, PatchesList, PatchesConfig


def main():
  args = parse_args()

  directory = args.directory
  force = args.force
  patches = args.patch
  repo = args.repo
  reverse = args.reverse

  if directory:
    (success, failed_patches) = apply_patches_from_directory(directory, force, reverse)
  else:
    (success, failed_patches) = apply_patches(repo, patches, force, reverse)

  if success:
    print 'Done: All patches applied.'
  else:
    failed_patches_paths = [p.get_file_path() for p in failed_patches]
    print 'Error: {0} patch(es) failed:\n{1}'.format(len(failed_patches), '\n'.join(failed_patches_paths))

  return 0 if success else 1


def apply_patches(repo_path, patches_paths, force=False, reverse=False):
  patches = [Patch(os.path.abspath(patch_path), os.path.abspath(repo_path)) for patch_path in patches_paths]
  patches_list = PatchesList(patches)
  stop_on_error = not force
  return patches_list.apply(reverse=reverse, stop_on_error=stop_on_error)


def apply_patches_from_directory(directory, force=False, reverse=False):
  config = PatchesConfig.from_directory(directory)
  patches_list = config.get_patches_list()

  # Notify user if we didn't find any patch files.
  if patches_list is None or len(patches_list) == 0:
    print 'Warning: No patches found in the "{0}" folder.'.format(directory)
    return (True, [])

  # Then try to apply patches.
  stop_on_error = not force
  return patches_list.apply(reverse=reverse, stop_on_error=stop_on_error)


def parse_args():
  parser = argparse.ArgumentParser(description='Apply patches to a git repo')
  parser.add_argument('-f', '--force', default=False, action='store_true',
                      help='Do not stop on the first failed patch.')
  parser.add_argument('-R', '--reverse', default=False, action='store_true', help='Apply patches in reverse.')
  parser.add_argument('-r', '--repo', help='Path to a repository root folder.')

  paths_group = parser.add_mutually_exclusive_group(required=True)
  paths_group.add_argument('-d', '--directory',
                           help='Path to a directory with patches. If present, -p/--patch is ignored.')
  paths_group.add_argument('-p', '--patch', nargs='*', help='Path(s) to a patch file(s).')

  args = parser.parse_args()

  # Additional rules.
  if args.patch is not None and args.repo is None:
    parser.error("Repository path (-r/--repo) is required when you supply patches list.")

  return args


if __name__ == '__main__':
  sys.exit(main())
