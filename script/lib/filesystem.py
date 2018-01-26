"""Filesystem related helper functions.
"""

import errno
import os
import shutil


def mkdir_p(path):
  try:
    os.makedirs(path)
  except OSError as e:
    if e.errno != errno.EEXIST:
      raise


def rm_f(path):
  try:
    os.remove(path)
  except OSError as e:
    if e.errno != errno.ENOENT:
      raise


def rm_rf(path):
  try:
    shutil.rmtree(path)
  except OSError as e:
    if e.errno != errno.ENOENT:
      raise


def safe_unlink(path):
  try:
    os.unlink(path)
  except OSError as e:
    if e.errno != errno.ENOENT:
      raise
