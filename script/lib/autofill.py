#!/usr/bin/env python

import os

BINARIES = {
  'darwin': [
    'libaddressinput_util.a',
    'libautofill_content_browser.a',
    'libautofill_content_common.a',
    'libautofill_content_mojo_bindings.a',
    'libautofill_content_renderer.a',
    'libautofill_core_browser.a',
    'libautofill_core_common.a',
    'libautofill_server_proto.a',
    'libos_crypt.a',
    'libdata_use_measurement_core.a',
    'libgoogle_apis.a',
    'libphonenumber.a',
    'libphonenumber_without_metadata.a',
    'libsignin_core_browser.a',
    'libsignin_core_common.a',
  ],
  'linux': [
    'libaddressinput_util.a',
    'libautofill_content_browser.a',
    'libautofill_content_common.a',
    'libautofill_content_mojo_bindings.a',
    'libautofill_content_renderer.a',
    'libautofill_core_browser.a',
    'libautofill_core_common.a',
    'libautofill_server_proto.a',
    'libos_crypt.a',
    'libdata_use_measurement_core.a',
    'libgoogle_apis.a',
    'libphonenumber.a',
    'libphonenumber_without_metadata.a',
    'libsignin_core_browser.a',
    'libsignin_core_common.a',
  ],
  'win32': [
    os.path.join('obj', 'third_party', 'libaddressinput', 'libaddressinput_util.lib'),
    os.path.join('obj', 'components', 'autofill_content_browser.lib'),
    os.path.join('obj', 'components', 'autofill_content_common.lib'),
    os.path.join('obj', 'components', 'autofill_content_mojo_bindings.lib'),
    os.path.join('obj', 'components', 'autofill_content_renderer.lib'),
    os.path.join('obj', 'components', 'autofill_core_browser.lib'),
    os.path.join('obj', 'components', 'autofill_core_common.lib'),
    os.path.join('obj', 'components', 'autofill_server_proto.lib'),
    os.path.join('obj', 'components', 'os_crypt.lib'),
    os.path.join('obj', 'components', 'data_use_measurement_core.lib'),
    os.path.join('obj', 'google_apis', 'google_apis.lib'),
    os.path.join('obj', 'third_party', 'libphonenumber', 'libphonenumber.lib'),
    os.path.join('obj', 'third_party', 'libphonenumber', 'libphonenumber_without_metadata.lib'),
    os.path.join('obj', 'components', 'signin_core_browser.lib'),
    os.path.join('obj', 'components', 'signin_core_common.lib'),
  ],
}

INCLUDE_DIRS = [
  'google_apis/gaia',
  'sql',
  'third_party/protobuf',
  'components/autofill',
  'components/webdata',
]
GENERATED_INCLUDE_DIRS = [
  'components/autofill',
  'protoc_out/components/autofill',
]
OTHER_HEADERS = [
  'chrome/browser/sync/glue/sync_start_util.h',
]
