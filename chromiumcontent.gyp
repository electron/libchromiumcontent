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
        ['OS=="linux"', {
          'dependencies': [
            '<(DEPTH)/sandbox/sandbox.gyp:chrome_sandbox',
            '<(DEPTH)/testing/gtest.gyp:gtest',
            '<(DEPTH)/net/net.gyp:net_test_support',
            '<(DEPTH)/components/components.gyp:encryptor',
          ],
        }],
        ['OS=="win"', {
          'dependencies': [
            'chromiumviews',
            '<(DEPTH)/components/components.gyp:encryptor',
            '<(DEPTH)/sandbox/sandbox.gyp:sandbox_static',
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
        ['OS=="win"', {
          'sources': [
            '<(DEPTH)/base/win/dllmain.cc',
          ],
          'configurations': {
            'Common_Base': {
              'msvs_settings': {
                'VCLinkerTool': {
                  'AdditionalOptions': [
                    '/WX', # Warnings as errors
                  ],
                },
              },
            },
            'Debug_Base': {
              'msvs_settings': {
                'VCLinkerTool': {
                  # We're too big to link incrementally. chrome.dll turns this
                  # off in (most? all?) cases, too.
                  'LinkIncremental': '1',
                },
              },
            },
          },
        }],
        ['OS=="mac"', {
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
      'conditions': [
        ['OS=="mac"', {
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
        }],
        ['OS=="win"', {
          'actions': [
            {
              'action_name': 'Create test_support_chromiumcontent.lib',
              'inputs': [
                '<(PRODUCT_DIR)\\obj\\base\\base_prefs_test_support.lib',
                '<(PRODUCT_DIR)\\obj\\base\\test_support_base.lib',
                '<(PRODUCT_DIR)\\obj\\content\\test_support_content.lib',
                '<(PRODUCT_DIR)\\obj\\net\\net_test_support.lib',
                '<(PRODUCT_DIR)\\obj\\testing\\gmock.lib',
                '<(PRODUCT_DIR)\\obj\\testing\\gtest.lib',
                '<(PRODUCT_DIR)\\obj\\ui\\ui_test_support.lib',
              ],
              'outputs': [
                '<(PRODUCT_DIR)\\test_support_chromiumcontent.lib',
              ],
              'action': [
                'lib.exe',
                '/nologo',
                # We can't use <(_outputs) here because that escapes the
                # backslash in the path, which confuses lib.exe.
                '/OUT:<(PRODUCT_DIR)\\test_support_chromiumcontent.lib',
                '<@(_inputs)',
              ],
              'msvs_cygwin_shell': 0,
            },
          ],
        }],
      ],
    },
  ],
  'conditions': [
    ['OS=="win"', {
      'targets': [
        {
          'target_name': 'chromiumviews',
          'type': 'none',
          'dependencies': [
            '<(DEPTH)/ui/views/controls/webview/webview.gyp:webview',
            '<(DEPTH)/ui/views/views.gyp:views',
          ],
          'actions': [
            {
              'action_name': 'Create chromiumviews.lib',
              'inputs': [
                '<(PRODUCT_DIR)\\obj\\third_party\\iaccessible2\\iaccessible2.lib',
                '<(PRODUCT_DIR)\\obj\\ui\\compositor\\compositor.lib',
                '<(PRODUCT_DIR)\\obj\\ui\\views\\views.lib',
                '<(PRODUCT_DIR)\\obj\\ui\\views\\controls\\webview\\webview.lib',
                '<(PRODUCT_DIR)\\obj\\ui\\web_dialogs\\web_dialogs.lib',
              ],
              'outputs': [
                '<(PRODUCT_DIR)\\chromiumviews.lib',
              ],
              'action': [
                'lib.exe',
                '/nologo',
                # We can't use <(_outputs) here because that escapes the
                # backslash in the path, which confuses lib.exe.
                '/OUT:<(PRODUCT_DIR)\\chromiumviews.lib',
                '<@(_inputs)',
              ],
              'msvs_cygwin_shell': 0,
            },
          ],
        },
      ],
    }],
  ],
}
