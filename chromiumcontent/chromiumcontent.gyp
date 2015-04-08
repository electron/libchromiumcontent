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
            '<(DEPTH)/third_party/mesa/mesa.gyp:osmesa',
          ],
        }],
        ['OS=="win"', {
          'dependencies': [
            'chromiumviews',
          ],
        }],
      ],
    },
    {
      'target_name': 'chromiumcontent',
      # Build chromiumcontent as shared_library otherwise some static libraries
      # will not build.
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
    },
  ],
  'conditions': [
    ['OS in ["win", "linux"]', {
      'targets': [
        {
          'target_name': 'chromiumviews',
          'type': 'shared_library',
          'dependencies': [
            '<(DEPTH)/ui/content_accelerators/ui_content_accelerators.gyp:ui_content_accelerators',
            '<(DEPTH)/ui/display/display.gyp:display',
            '<(DEPTH)/ui/display/display.gyp:display_util',
            '<(DEPTH)/ui/views/controls/webview/webview.gyp:webview',
            '<(DEPTH)/ui/views/views.gyp:views',
            '<(DEPTH)/ui/wm/wm.gyp:wm',
          ],
          'conditions': [
            ['OS=="linux"', {
              'dependencies': [
                '<(DEPTH)/chrome/browser/ui/libgtk2ui/libgtk2ui.gyp:gtk2ui',
              ],
            }],  # OS=="linux"
          ],
        },
      ],
    }],
  ],
}
