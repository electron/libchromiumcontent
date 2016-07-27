#!/usr/bin/env python

import os
import glob
import shutil
import lib.util
from lib.config import get_configuration

SOURCE_ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), '..'))
DIST_DIR = os.path.join(SOURCE_ROOT, 'dist')
MAIN_DIR = os.path.join(DIST_DIR, 'main')

BINARIES = {
  'all': [
    os.path.join('gen', 'extensions', 'extensions_resources.pak'),
    os.path.join('gen', 'extensions', 'extensions_renderer_resources.pak'),
    os.path.join('gen', 'chrome', 'extensions_api_resources.pak'),
  ],
  'darwin': [
    'libapi_gen_util.a',
    'libbrowsing_data.a',
    'libchrome_api.a',
    'libchrome_zlib.a',
    'libcld2_static.a',
    'libcontent_settings_core_common.a',
    'libcrx_file.a',
    'libdevice_usb.a',
    'libextensions_api.a',
    'libextensions_api_registration.a',
    'libextensions_browser.a',
    'libextensions_common.a',
    'libextensions_common_constants.a',
    'libextensions_renderer.a',
    'libextensions_utility.a',
    'libguest_view_browser.a',
    'libguest_view_common.a',
    'libguest_view_renderer.a',
    'libleveldatabase.a',
    'libmojo_cpp_system.a',
    'libmojo_cpp_bindings.a',
    'libmojo_js_bindings.a',
    'libpref_registry.a',
    'libre2.a',
    'libsnappy.a',
    'libsyncable_prefs.a',
    'libui_zoom.a',
    'libvariations.a',
    'libweb_cache_browser.a',
    'libweb_cache_mojo_bindings.a',
    'libweb_modal.a',
    'libxml2.a',
    'libzlib_x86_simd.a',
  ],
  'linux': [
    'libapi_gen_util.a',
    'libbrowsing_data.a',
    'libchrome_api.a',
    'libchrome_zlib.a',
    'libcld2_static.a',
    'libcontent_settings_core_common.a',
    'libcrx_file.a',
    'libdevice_usb.a',
    'libextensions_api.a',
    'libextensions_api_registration.a',
    'libextensions_browser.a',
    'libextensions_common.a',
    'libextensions_common_constants.a',
    'libextensions_renderer.a',
    'libextensions_utility.a',
    'libguest_view_browser.a',
    'libguest_view_common.a',
    'libguest_view_renderer.a',
    'libleveldatabase.a',
    'libmojo_cpp_system.a',
    'libmojo_cpp_bindings.a',
    'libmojo_js_bindings.a',
    'libpref_registry.a',
    'libre2.a',
    'libsnappy.a',
    'libsyncable_prefs.a',
    'libui_zoom.a',
    'libvariations.a',
    'libweb_cache_browser.a',
    'libweb_cache_mojo_bindings.a',
    'libweb_modal.a',
    'libxml2.a',
    'libzlib_x86_simd.a',
  ],
  'win32': [
    os.path.join('obj', 'tools', 'json_schema_compiler', 'api_gen_util.lib'),
    os.path.join('obj', 'components', 'browsing_data.lib'),
    os.path.join('obj', 'chrome', 'common', 'extensions', 'api', 'chrome_api.lib'),
    os.path.join('obj', 'third_party', 'cld_2', 'cld2_static.lib'),
    os.path.join('obj', 'components', 'content_settings_core_common.lib'),
    os.path.join('obj', 'components', 'crx_file.lib'),
    os.path.join('obj', 'device', 'usb', 'device_usb.lib'),
    os.path.join('obj', 'extensions', 'common', 'api', 'extensions_api.lib'),
    os.path.join('obj', 'extensions', 'browser', 'api', 'extensions_api_registration.lib'),
    os.path.join('obj', 'extensions', 'extensions_browser.lib'),
    os.path.join('obj', 'extensions', 'extensions_common.lib'),
    os.path.join('obj', 'extensions', 'extensions_common_constants.lib'),
    os.path.join('obj', 'extensions', 'extensions_renderer.lib'),
    os.path.join('obj', 'extensions', 'extensions_utility.lib'),
    os.path.join('obj', 'components', 'guest_view_browser.lib'),
    os.path.join('obj', 'components', 'guest_view_common.lib'),
    os.path.join('obj', 'components', 'guest_view_renderer.lib'),
    os.path.join('obj', 'third_party', 'leveldatabase', 'leveldatabase.lib'),
    os.path.join('obj', 'mojo', 'mojo_cpp_system.lib'),
    os.path.join('obj', 'mojo', 'mojo_cpp_bindings.lib'),
    os.path.join('obj', 'mojo', 'mojo_js_bindings.lib'),
    os.path.join('obj', 'components', 'pref_registry.lib'),
    os.path.join('obj', 'third_party', 're2', 're2.lib'),
    os.path.join('obj', 'third_party', 'snappy', 'snappy.lib'),
    os.path.join('obj', 'components', 'syncable_prefs.lib'),
    os.path.join('obj', 'components', 'ui_zoom.lib'),
    os.path.join('obj', 'components', 'variations.lib'),
    os.path.join('obj', 'components', 'web_cache_browser.lib'),
    os.path.join('obj', 'components', 'web_cache_mojo_bindings.lib'),
    os.path.join('obj', 'components', 'web_modal.lib'),
    os.path.join('obj', 'third_party', 'libxml', 'libxml2.lib'),
    os.path.join('obj', 'third_party', 'zlib', 'zlib_x86_simd.lib')
  ],
}

INCLUDE_DIRS = [
  'extensions/browser',
  'extensions/common',
  'extensions/components',
  'extensions/renderer',
  'extensions/strings',
  'extensions/utility',
  'sync/api',
  'sync/base',
  'sync/internal_api',
  'components/content_settings',
  'components/user_prefs',
  'components/pref_registry',
  'components/syncable_prefs',
  'components/keyed_service',
  'components/web_modal',
  'components/crx_file',
]
GENERATED_INCLUDE_DIRS = [
  'chrome',
  'extensions',
  'services',
]
OTHER_HEADERS = [
  'chrome/common/chrome_isolated_world_ids.h',
]
OTHER_DIRS = [
  'build',
  'tools/grit',
]

def copy_extension_locales(target_arch, component, output_dir):
  config = get_configuration(target_arch)
  target_dir = os.path.join(MAIN_DIR, component, 'locales')
  src_dir = os.path.join(output_dir, config, 'gen', 'extensions', 'strings', 'extension_strings')
  for src_file in glob.glob(os.path.join(src_dir, 'extension_strings_*.pak')):
    filename = os.path.basename(src_file)
    new_name = re.sub('extension_strings_', '', filename)
    shutil.copy2(src_file, os.path.join(target_dir, new_name))

