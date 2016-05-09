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
        '<(DEPTH)/components/prefs/prefs.gyp:prefs',
        '<(DEPTH)/components/components.gyp:cdm_renderer',
        '<(DEPTH)/components/components.gyp:devtools_discovery',
        '<(DEPTH)/components/components.gyp:devtools_http_handler',
        '<(DEPTH)/components/components.gyp:security_state',
        '<(DEPTH)/content/content.gyp:content',
        '<(DEPTH)/content/content.gyp:content_app_both',
        '<(DEPTH)/content/content_shell_and_tests.gyp:content_shell_pak',
        '<(DEPTH)/net/net.gyp:net_with_v8',
        '<(DEPTH)/ppapi/ppapi_internal.gyp:ppapi_host',
        '<(DEPTH)/ppapi/ppapi_internal.gyp:ppapi_proxy',
        '<(DEPTH)/ppapi/ppapi_internal.gyp:ppapi_ipc',
        '<(DEPTH)/ppapi/ppapi_internal.gyp:ppapi_shared',
        '<(DEPTH)/third_party/mojo/mojo_public.gyp:mojo_cpp_bindings',
        '<(DEPTH)/third_party/mojo/mojo_public.gyp:mojo_environment_standalone',
        '<(DEPTH)/third_party/mojo/mojo_public.gyp:mojo_system',
        '<(DEPTH)/third_party/mojo/mojo_public.gyp:mojo_utility',
        '<(DEPTH)/third_party/webrtc/modules/modules.gyp:desktop_capture',
        '<(DEPTH)/third_party/widevine/cdm/widevine_cdm.gyp:widevinecdmadapter',
        '<(DEPTH)/third_party/widevine/cdm/widevine_cdm.gyp:widevine_cdm_version_h',
      ],
      'sources': [
        'empty.cc',
      ],
      'conditions': [
        ['OS=="win"', {
          'dependencies': [
            '<(DEPTH)/pdf/pdf.gyp:pdf',
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
