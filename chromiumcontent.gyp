{
  'targets': [
    {
      'target_name': 'chromiumcontent_all',
      'type': 'none',
      'dependencies': [
        'chromiumcontent',
        'test_support_chromiumcontent',
      ],
      'conditions': [
        ['OS=="win"', {
          'dependencies!': [
            'test_support_chromiumcontent',
          ],
        }],
      ],
    },
    {
      'target_name': 'chromiumcontent',
      'type': 'shared_library',
      'dependencies': [
        '<(DEPTH)/base/base.gyp:base_prefs',
        '<(DEPTH)/content/content.gyp:content',
        '<(DEPTH)/content/content.gyp:content_shell_pak',
      ],
      'conditions': [
        ['OS=="mac"', {
          'dependencies': [
            'chrome_browser_ui',
          ],
          'xcode_settings': {
            'OTHER_LDFLAGS': [
              '-all_load',
            ],
            'LD_DYLIB_INSTALL_NAME': '@rpath/libchromiumcontent.dylib',
          },
        }],
      ],
    },
    {
      'target_name': 'test_support_chromiumcontent',
      'type': 'none',
      'dependencies': [
        '<(DEPTH)/base/base.gyp:base_prefs_test_support',
        '<(DEPTH)/content/content.gyp:test_support_content',
      ],
      'actions': [
        {
          'action_name': 'Create libtest_support_chromiumcontent.a',
          'inputs': [
            '<(PRODUCT_DIR)/libbase_prefs_test_support.a',
            '<(PRODUCT_DIR)/libgmock.a',
            '<(PRODUCT_DIR)/libgtest.a',
            '<(PRODUCT_DIR)/libnet_test_support.a',
            '<(PRODUCT_DIR)/libtest_support_base.a',
            '<(PRODUCT_DIR)/libtest_support_content.a',
            '<(PRODUCT_DIR)/libui_test_support.a',
          ],
          'outputs': [
            '<(PRODUCT_DIR)/libtest_support_chromiumcontent.a',
          ],
          'action': [
            '/usr/bin/libtool',
            '-static',
            '-o',
            '<@(_outputs)',
            '<@(_inputs)',
          ],
        },
      ],
    },
  ],
  'conditions': [
    ['OS=="mac"', {
      'targets': [
        {
          'target_name': 'chrome_browser_ui',
          'type': 'static_library',
          'sources': [
            '<(DEPTH)/chrome/browser/ui/cocoa/event_utils.h',
            '<(DEPTH)/chrome/browser/ui/cocoa/event_utils.mm',
            '<(DEPTH)/chrome/browser/ui/cocoa/menu_controller.h',
            '<(DEPTH)/chrome/browser/ui/cocoa/menu_controller.mm',
          ],
          'dependencies': [
            # Import Skia's include_dirs for finding the SkUserConfig.h,
            '<(DEPTH)/skia/skia.gyp:skia',
            # and ICU for unicode/*.h.
            '<(DEPTH)/third_party/icu/icu.gyp:icui18n',
            '<(DEPTH)/third_party/icu/icu.gyp:icuuc',
          ],
          'include_dirs': [
            '<(DEPTH)'
          ],
          'xcode_settings': {
            # Export all symbols from this static library even though they aren't
            # specified to be exported in the source code.
            'GCC_INLINES_ARE_PRIVATE_EXTERN': 'NO',
            'GCC_SYMBOLS_PRIVATE_EXTERN': 'NO',
          },
        },
      ],
    }],
  ],
}
