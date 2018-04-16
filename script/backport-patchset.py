#!/usr/bin/env python

import os
import re
import sys
import urllib2

SOURCE_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
PATCHES_DIR = os.path.join(SOURCE_ROOT, 'patches')

def main():
  if len(sys.argv) < 3:
    print("Usage: backport-patchset.py [code-review-id] [patch-name]")
    return 1
  codereview_url = "https://codereview.chromium.org/" + sys.argv[1]

  codereview_response = urllib2.urlopen(codereview_url)
  codereview = codereview_response.read()
  diff_url_re = re.compile("/download/issue" + sys.argv[1] + "_[0-9]+\.diff", re.MULTILINE)
  diff_url_result = diff_url_re.search(codereview)
  if diff_url_result is None:
    print("Failed to find diff for: " + sys.argv[1])
    return 1
  diff_url = "https://codereview.chromium.org" + diff_url_result.group(0)

  diff_response = urllib2.urlopen(diff_url)
  diff_content = diff_response.read()
  diff_lines = diff_content.split("\n")[1:]
  diffs = []
  current_diff = []
  for current_diff_line in diff_lines:
    if re.match('Index: ', current_diff_line) is not None:
      diffs.append(current_diff)
      current_diff = []
    else:
      current_diff.append(current_diff_line)
  diffs.append(current_diff)
  for i in range(len(diffs)):
    diffs[i] = '\n'.join(diffs[i])

  patch_file = os.path.join(PATCHES_DIR, get_next_patch_number(PATCHES_DIR) + "-" + sys.argv[2] + ".patch")
  with open(patch_file, "w") as file:
    file.write("# Backported patch from Chromium Patchset: " + codereview_url + "\n")
    file.write('\n'.join(diffs))
  print("Wrote new patch file: " + os.path.relpath(patch_file, SOURCE_ROOT))
  return 0

def get_next_patch_number(patch_dir):
  max_patch = 0
  for patch_file in os.listdir(patch_dir):
    path_file_path = os.path.join(patch_dir, patch_file)
    if not os.path.isfile(path_file_path):
      continue
    patch_number = int(patch_file[:3])
    max_patch = max(patch_number, max_patch)
  return '%03d' % (max_patch + 1,)

if __name__ == '__main__':
    sys.exit(main())
