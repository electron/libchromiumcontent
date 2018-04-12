"""Git helper functions.

Everything in here should be project agnostic, shouldn't rely on project's structure,
and make any assumptions about the passed arguments or calls outcomes.
"""

import subprocess

from util import scoped_cwd


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


def get_patch(repo, commit_hash):
  args = ['git', 'diff-tree',
          '-p',
          commit_hash,
          '--'  # Explicitly tell Git that `commit_hash` is a revision, not a path.
          ]

  with scoped_cwd(repo):
    return subprocess.check_output(args)


def get_head_commit(repo):
  args = ['git', 'rev-parse', 'HEAD']

  with scoped_cwd(repo):
    return subprocess.check_output(args).strip()
