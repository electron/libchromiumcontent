"""Git helper functions.

Everything in here should be project agnostic, shouldn't rely on project's structure,
and make any assumptions about the passed arguments or calls outcomes.
"""

import os
import subprocess

from util import scoped_cwd


def is_repo_root(path):
  path_exists = os.path.exists(path)
  if not path_exists:
    return False

  git_folder_path = os.path.join(path, '.git')
  git_folder_exists = os.path.exists(git_folder_path)

  return git_folder_exists


def get_repo_root(path):
  """Finds a closest ancestor folder which is a repo root."""
  norm_path = os.path.normpath(path)
  norm_path_exists = os.path.exists(norm_path)
  if not norm_path_exists:
    return None

  if is_repo_root(norm_path):
    return norm_path

  parent_path = os.path.dirname(norm_path)

  # Check if we're in the root folder already.
  if parent_path == norm_path:
    return None

  return get_repo_root(parent_path)


def apply(repo, patch_path, directory=None, index=False, reverse=False):
  args = ['git', 'apply',
          '--ignore-space-change',
          '--ignore-whitespace',
          '--whitespace', 'fix'
          ]
  if directory:
    args += ['--directory', directory]
  if index:
    args += ['--index']
  if reverse:
    args += ['--reverse']
  args += ['--', patch_path]

  with scoped_cwd(repo):
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


commits = {}

def prepare_commit(repo, author, message):
  global commits
  """ Commit whatever in the index is now."""

  if repo not in commits:
    commits[repo] = []
    
  commits[repo].append((author, message))

  return True

def finalize_commits():
  global commits
  print('\n\nfinalizing commits')
  # Let's setup committer info so git won't complain about it being missing.
  # TODO: Is there a better way to set committer's name and email?
  env = os.environ.copy()
  env['GIT_COMMITTER_NAME'] = 'Anonymous Committer'
  env['GIT_COMMITTER_EMAIL'] = 'anonymous@electronjs.org'

  committed_successfully = True

  for repo in commits:
    details = commits[repo]
    # Skip the commit when nothing to commit
    if len(details) == 0:
      continue

    # Reset the list of commits for next time
    commits[repo] = []
    generated_message = 'Applied ' + str(len(details)) + ' Electron Patches\n\n'

    for item in details:
      generated_message += 'Author: ' + item[0] + '\n' + 'Message: ' + item[1] + '\n\n'

    args = ['git', 'commit',
            '--author', 'Electron Build Process <build@electronjs.org>',
            '--message', generated_message,
            '-n'
            ]

    with scoped_cwd(repo):
      return_code = subprocess.call(args, env=env)
      if not (return_code == 0):
        print('failed to commit', repo)
      committed_successfully = (return_code == 0) and committed_successfully

  return committed_successfully
