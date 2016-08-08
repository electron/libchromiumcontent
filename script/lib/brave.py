#!/usr/bin/env python

import lib.extensions
from lib.extensions import copy_extension_locales
import lib.autofill

BINARIES = lib.extensions.BINARIES
BINARIES['darwin'] = BINARIES['darwin'] + lib.autofill.BINARIES['darwin']
BINARIES['linux'] = BINARIES['linux'] + lib.autofill.BINARIES['linux']
BINARIES['win32'] = BINARIES['win32'] + lib.autofill.BINARIES['win32']

INCLUDE_DIRS = lib.extensions.INCLUDE_DIRS + lib.autofill.INCLUDE_DIRS
GENERATED_INCLUDE_DIRS = lib.extensions.GENERATED_INCLUDE_DIRS + lib.autofill.GENERATED_INCLUDE_DIRS
OTHER_HEADERS = lib.extensions.OTHER_HEADERS + lib.autofill.OTHER_HEADERS
OTHER_DIRS = lib.extensions.OTHER_DIRS

def copy_brave_locales(target_arch, component, output_dir):
  copy_extension_locales(target_arch, component, output_dir)
