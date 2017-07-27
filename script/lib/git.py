"""Git helper functions.

Everything in here should be project agnostic, shouldn't rely on project's structure,
and make any assumptions about the passed arguments or calls outcomes.
"""

import subprocess


def apply(repo, patch_path, reverse=False):
  args = ['git', 'apply',
          '--directory', repo,
          '--ignore-space-change',
          '--ignore-whitespace',
          '--whitespace', 'fix'
          ]
  if reverse:
    args += ['--reverse']
  args += ['--', patch_path]

  return_code = subprocess.call(args)
  applied_successfully = (return_code == 0)

  return applied_successfully
