{
  'variables': {
    # We're not using Chromium's clang, so we can't use their plugins either.
    'clang_use_chrome_plugins': 0,
    # The Linux build of libchromiumcontent.so depends on, but doesn't
    # provide, tcmalloc by default.  Disabling tcmalloc here also prevents
    # any conflicts when linking to binaries or libraries that don't use
    # tcmalloc.
    'linux_use_tcmalloc': 0,
    'conditions': [
      ['OS=="win"', {
        # Chrome turns this off for component builds, and we need to too. Leaving
        # it on would result in both the Debug and Release CRTs being included in
        # the library.
        'win_use_allocator_shim': 0,

        'win_release_RuntimeLibrary': '2', # 2 = /MD (nondebug DLL)
        'win_debug_RuntimeLibrary': '3',   # 3 = /MDd (debug DLL)
      }],
    ],
  },
  'target_defaults': {
    'defines': [
      'ANGLE_TRANSLATOR_IMPLEMENTATION',
      'AURA_IMPLEMENTATION',
      'BASE_I18N_IMPLEMENTATION',
      'BASE_IMPLEMENTATION',
      'BASE_PREFS_IMPLEMENTATION',
      'BLINK_COMMON_IMPLEMENTATION',
      'BLINK_PLATFORM_IMPLEMENTATION',
      'BUILDING_V8_SHARED',
      'CC_IMPLEMENTATION',
      'COMPONENT_BUILD',
      'COMPOSITOR_IMPLEMENTATION',
      'CONTENT_IMPLEMENTATION',
      'CRYPTO_IMPLEMENTATION',
      'EVENTS_IMPLEMENTATION',
      'GFX_IMPLEMENTATION',
      'GL_IMPLEMENTATION',
      'GLES2_C_LIB_IMPLEMENTATION',
      'GLES2_IMPL_IMPLEMENTATION',
      'GLES2_UTILS_IMPLEMENTATION',
      'GPU_IMPLEMENTATION',
      'IPC_IMPLEMENTATION',
      'LIBPROTOBUF_EXPORTS',
      'LIBPROTOC_EXPORTS',
      'MEDIA_IMPLEMENTATION',
      'NATIVE_THEME_IMPLEMENTATION',
      'NET_IMPLEMENTATION',
      'PPAPI_HOST_IMPLEMENTATION',
      'PPAPI_PROXY_IMPLEMENTATION',
      'PPAPI_SHARED_IMPLEMENTATION',
      'PPAPI_THUNK_IMPLEMENTATION',
      'PRINTING_IMPLEMENTATION',
      'SHELL_DIALOGS_IMPLEMENTATION',
      'SKIA_DLL',
      'SKIA_IMPLEMENTATION',
      'SNAPSHOT_IMPLEMENTATION',
      'SQL_IMPLEMENTATION',
      'SURFACE_IMPLEMENTATION',
      'U_COMBINED_IMPLEMENTATION_EXCEPT_DATA',
      'U_NO_GLOBAL_NEW_DELETE',
      'U_UTF8_IMPL',
      'UI_IMPLEMENTATION',
      'URL_IMPLEMENTATION',
      'V8_SHARED',
      'WEBKIT_BASE_IMPLEMENTATION',
      'WEBKIT_CHILD_IMPLEMENTATION',
      'WEBKIT_COMMON_IMPLEMENTATION',
      'WEBKIT_COMPOSITOR_BINDINGS_IMPLEMENTATION',
      'WEBKIT_EXTENSIONS_IMPLEMENTATION',
      'WEBKIT_GLUE_IMPLEMENTATION',
      'WEBKIT_GPU_IMPLEMENTATION',
      'WEBKIT_IMPLEMENTATION',
      'WEBKIT_PLUGINS_IMPLEMENTATION',
      'WEBKIT_RENDERER_IMPLEMENTATION',
      'WEBKIT_STORAGE_BROWSER_IMPLEMENTATION',
      'WEBKIT_STORAGE_COMMON_IMPLEMENTATION',
      'WEBKIT_STORAGE_RENDERER_IMPLEMENTATION',
      'WEBKIT_USER_AGENT_IMPLEMENTATION',
      'WEBORIGIN_IMPLEMENTATION',
      'WTF_IMPLEMENTATION',
    ],
    'defines!': [
      '_HAS_EXCEPTIONS=0',
      'U_STATIC_IMPLEMENTATION',
    ],
    'msvs_disabled_warnings': [
        # class 'std::xx' needs to have dll-interface. Chrome turns this off
        # for component builds, and we need to too.
        4251,
    ],
    'msvs_settings': {
      'VCCLCompilerTool': {
        'ExceptionHandling': '1',  # /EHsc
      },
    },
    'xcode_settings': {
      'WARNING_CFLAGS!': [
        # Xcode 5 doesn't support -Wno-deprecated-register.
        '-Wno-deprecated-register',
      ],
    },
    'target_conditions': [
      ['_target_name=="base"', {
        # This file doesn't work inside a shared library, and won't compile at
        # all when COMPONENT_BUILD is defined.
        # We can't use sources! here because that generates path names relative
        # to this .gypi file, which won't match the relative path names in
        # base.gyp.
        'sources/': [
          ['exclude', 'debug/debug_on_start_win\.cc$'],
        ],
      }],
      # These targets get linked directly into client applications, so need
      # to see symbols decorated with __declspec(dllimport).
      ['_target_name in ["base_prefs_test_support", "net_test_support", "sandbox_static", "test_support_base", "test_support_content"]', {
        'defines!': [
          'BASE_IMPLEMENTATION',
          'CONTENT_IMPLEMENTATION',
          'NET_IMPLEMENTATION',
          'URL_IMPLEMENTATION',
        ],
      }],
      ['_target_name in ["compositor", "views", "webview", "web_dialogs"]', {
        'defines': [
          'VIEWS_IMPLEMENTATION',
          'WEBVIEW_IMPLEMENTATION',
          'WEB_DIALOGS_IMPLEMENTATION',
        ],
        'defines!': [
          'BASE_IMPLEMENTATION',
          'CC_IMPLEMENTATION',
          'CONTENT_IMPLEMENTATION',
          'GL_IMPLEMENTATION',
          'IPC_IMPLEMENTATION',
          'SKIA_IMPLEMENTATION',
          'UI_IMPLEMENTATION',
          'URL_IMPLEMENTATION',
        ],
      }],
      ['_target_name in ["v8", "v8_snapshot", "v8_shell", "preparser_lib"] or "v8_nosnapshot." in _target_name or "v8_base." in _target_name or "mksnapshot." in _target_name', {
        # Override src/v8/build/common.gypi's RuntimeLibrary setting.
        'configurations': {
          'Debug': {
            'msvs_settings': {
              'VCCLCompilerTool': {
                'RuntimeLibrary': '<(win_debug_RuntimeLibrary)',
              },
            },
          },
          'Release': {
            'msvs_settings': {
              'VCCLCompilerTool': {
                'RuntimeLibrary': '<(win_release_RuntimeLibrary)',
              },
            },
          },
        },
      }],
    ],
  },
}
