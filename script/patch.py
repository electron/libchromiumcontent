#!/usr/bin/env python
"""
Usage: patch -h

Use this script to selectively apply and revert patches.
It is mostly useful to fix patches during upgrades to a new Chromium version.
"""

import argparse
import os
import subprocess
import sys

from lib.git import apply as git_apply


def main():
  args = parse_args()

  directory = args.directory
  force = args.force
  patches = args.patch
  repo = args.repo
  reverse = args.reverse

  if directory:
    (all_patches_applied, failed_patches) = apply_patches_from_directory(repo, directory, force, reverse)
  else:
    (all_patches_applied, failed_patches) = apply_patches(repo, patches, force, reverse)

  if all_patches_applied:
    print 'Done: All patches applied.'
  else:
    print 'Error: {0} patch(es) failed:\n{1}'.format(len(failed_patches), '\n'.join(failed_patches))

  return all_patches_applied


def apply_patches(repo, patches_paths, force=False, reverse=False):
  all_patches_applied = True
  failed_patches = []

  for patch_path in patches_paths:
    applied_successfully = git_apply(repo, patch_path, reverse=reverse)

    if not applied_successfully:
      all_patches_applied = False
      failed_patches.append(patch_path)

    should_stop_now = not applied_successfully and not force
    if should_stop_now:
      break

  return (all_patches_applied, failed_patches)


def apply_patches_from_directory(repo, directory, force=False, reverse=False):
  # First, get list of ".patch" files.
  directory_children = [os.path.join(directory, child) for child in os.listdir(directory)]
  patch_files = [path for path in directory_children if os.path.isfile(path) and path.endswith('.patch')]

  # Notify user if we didn't find any patch files.
  if len(patch_files) == 0:
    print 'Warning: No "*.patch" files found in the "{0}" folder.'.format(directory)
    return (True, [])

  # Then try to apply patches.
  sorted_patch_files = sorted(patch_files, reverse=reverse)
  return apply_patches(repo, sorted_patch_files, force=force, reverse=reverse)


def parse_args():
  parser = argparse.ArgumentParser(description='Apply patches to a git repo')
  parser.add_argument('-f', '--force', default=False, action='store_true',
                      help='Do not stop on the first failed patch.')
  parser.add_argument('-R', '--reverse', default=False, action='store_true', help='Apply patches in reverse.')
  parser.add_argument('-r', '--repo', required=True, help='Path to a repository root folder.')

  paths_group = parser.add_mutually_exclusive_group(required=True)
  paths_group.add_argument('-d', '--directory',
                           help='Path to a directory with "*.patch" files. If present, -p/--patch is ignored.')
  paths_group.add_argument('-p', '--patch', nargs='*', help='Path(s) to a patch file(s).')

  return parser.parse_args()


if __name__ == '__main__':
  sys.exit(main())
