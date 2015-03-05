{
  'targets': [
    {
      'target_name': 'chromiumcontent_all',
      'type': 'none',
      'dependencies': [
        'chromiumcontent',
        '<(DEPTH)/chrome/chrome.gyp:chromedriver',
      ],
      'conditions': [
        ['OS=="linux"', {
          'dependencies': [
            'chromiumviews',
            '<(DEPTH)/build/linux/system.gyp:libspeechd',
            '<(DEPTH)/sandbox/sandbox.gyp:chrome_sandbox',
            '<(DEPTH)/components/components.gyp:os_crypt',
            '<(DEPTH)/third_party/mesa/mesa.gyp:osmesa',
          ],
          'actions': [
            {
              'action_name': 'Flatten libos_crypt.a',
              'inputs': [
                '<(PRODUCT_DIR)/obj/components/libos_crypt.a',
              ],
              'outputs': [
                '<(PRODUCT_DIR)/libos_crypt.a',
              ],
              'action': [
                '<(DEPTH)/../../../tools/linux/ar-combine.sh',
                '-o',
                '<@(_outputs)',
                '<@(_inputs)',
              ],
            },
            {
              'action_name': 'Flatten libspeechd.a',
              'inputs': [
                '<(PRODUCT_DIR)/obj/build/linux/libspeechd.a',
              ],
              'outputs': [
                '<(PRODUCT_DIR)/libspeechd.a',
              ],
              'action': [
                '<(DEPTH)/../../../tools/linux/ar-combine.sh',
                '-o',
                '<@(_outputs)',
                '<@(_inputs)',
              ],
            },
          ],
        }],
        ['OS=="win"', {
          'dependencies': [
            'chromiumviews',
            '<(DEPTH)/components/components.gyp:os_crypt',
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
        '<(DEPTH)/content/content.gyp:content_app_both',
        '<(DEPTH)/content/content_shell_and_tests.gyp:content_shell_pak',
        '<(DEPTH)/net/net.gyp:net_with_v8',
      ],
      'sources': [
        'empty.cc',
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
          'variables': {
            # Create a fake .dSYM in Release mode that we can then post-process
            # to create a real dSYM in script/create-dist.
            'mac_strip': 1,
          },
          'xcode_settings': {
            'OTHER_LDFLAGS': [
              '-all_load',
            ],
            'LD_DYLIB_INSTALL_NAME': '@rpath/libchromiumcontent.dylib',
          },
        }],
        ['OS=="linux" and host_arch=="ia32"', {
          'target_conditions': [
            ['_toolset=="target"', {
              'ldflags': [
                # Workaround for linker OOM.
                '-Wl,--no-keep-memory',
              ],
            }],
          ],
        }],
      ],
    },
  ],
  'conditions': [
    ['OS in ["win", "linux"]', {
      'targets': [
        {
          'target_name': 'chromiumviews',
          'type': 'none',
          'dependencies': [
            '<(DEPTH)/ui/display/display.gyp:display',
            '<(DEPTH)/ui/display/display.gyp:display_util',
            '<(DEPTH)/ui/views/controls/webview/webview.gyp:webview',
            '<(DEPTH)/ui/views/views.gyp:views',
            '<(DEPTH)/ui/wm/wm.gyp:wm',
          ],
          'conditions': [
            ['OS=="win"', {
              'actions': [
                {
                  'action_name': 'Create chromiumviews.lib',
                  'inputs': [
                    '<(PRODUCT_DIR)\\obj\\third_party\\iaccessible2\\iaccessible2.lib',
                    '<(PRODUCT_DIR)\\obj\\ui\\display\\display.lib',
                    '<(PRODUCT_DIR)\\obj\\ui\\display\\display_util.lib',
                    '<(PRODUCT_DIR)\\obj\\ui\\views\\views.lib',
                    '<(PRODUCT_DIR)\\obj\\ui\\views\\controls\\webview\\webview.lib',
                    '<(PRODUCT_DIR)\\obj\\ui\\web_dialogs\\web_dialogs.lib',
                    '<(PRODUCT_DIR)\\obj\\ui\\wm\\wm.lib',
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
            }],  # OS=="win"
            ['OS=="linux"', {
              'dependencies': [
                '<(DEPTH)/chrome/browser/ui/libgtk2ui/libgtk2ui.gyp:gtk2ui',
              ],
              'actions': [
                {
                  'action_name': 'Create libchromiumviews.a',
                  'inputs': [
                    '<(PRODUCT_DIR)/obj/chrome/browser/ui/libgtk2ui/libgtk2ui.a',
                    '<(PRODUCT_DIR)/obj/ui/display/libdisplay.a',
                    '<(PRODUCT_DIR)/obj/ui/display/libdisplay_util.a',
                    '<(PRODUCT_DIR)/obj/ui/views/libviews.a',
                    '<(PRODUCT_DIR)/obj/ui/views/controls/webview/libwebview.a',
                    '<(PRODUCT_DIR)/obj/ui/web_dialogs/libweb_dialogs.a',
                    '<(PRODUCT_DIR)/obj/ui/wm/libwm.a',
                  ],
                  'outputs': [
                    '<(PRODUCT_DIR)/libchromiumviews.a',
                  ],
                  'action': [
                    '<(DEPTH)/../../../tools/linux/ar-combine.sh',
                    '-o',
                    '<@(_outputs)',
                    '<@(_inputs)',
                  ],
                },
              ],
            }],  # OS=="linux"
          ],
        },
      ],
    }],
  ],
}
