{
  'targets': [
    {
      'target_name': 'chromiumcontent_all',
      'type': 'none',
      'dependencies': [
        'chromiumcontent',
      ],
      'conditions': [
        ['OS!="win"', {
          'dependencies': [
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
      'xcode_settings': {
        'OTHER_LDFLAGS': [
          '-all_load',
        ],
        'LD_DYLIB_INSTALL_NAME': '@rpath/libchromiumcontent.dylib',
      },
      'conditions': [
        ['OS=="win"', {
          'sources': [
            'dll_main.cc',
          ],
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
}
