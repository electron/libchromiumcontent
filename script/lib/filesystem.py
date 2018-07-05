"""Filesystem related helper functions.
"""

import contextlib
import errno
import os
import shutil
import sys
import tarfile
import tempfile
import urllib2


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

def byte_to_mb(n):
  return str(n / 1024 / 1024) + 'MB'

def download_and_extract(destination, url):
  print url
  with tempfile.TemporaryFile() as t:
    with contextlib.closing(urllib2.urlopen(url)) as u:
      total = int(u.headers['content-length'])
      done = 0
      while True:
        chunk = u.read(1024)
        done += len(chunk)
        if not len(chunk):
          break
        sys.stderr.write('                                   \r')
        percent = str(round(float(done) / float(total), 4) * 100) + '%'
        ratio = '(' + byte_to_mb(done) + '/' + byte_to_mb(total) + ')'
        sys.stderr.write(percent + ' ' + ratio + '\r')
        sys.stderr.flush()
        t.write(chunk)
    sys.stderr.write('\nExtracting...\n')
    sys.stderr.flush()
    with tarfile.open(fileobj=t, mode='r:bz2') as z:
      z.extractall(destination)
