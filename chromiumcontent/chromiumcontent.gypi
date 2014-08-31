{
  'variables': {
    # We're not using Chromium's clang, so we can't use their plugins either.
    'clang_use_chrome_plugins': 0,
    # And the gold's flags are not available in system's ld neither.
    'linux_use_gold_flags': 0,
    # Make Linux build contain debug symbols, this flag will add '-g' to cflags.
    'linux_dump_symbols': 1,
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
    'global_defines': [
      'COMPONENT_BUILD',
      'SKIA_DLL',
    ],
    'chromiumcontent_defines': [
      'ACCESSIBILITY_IMPLEMENTATION',
      'ANGLE_TRANSLATOR_IMPLEMENTATION',
      'APP_LIST_IMPLEMENTATION',
      'AURA_IMPLEMENTATION',
      'BASE_I18N_IMPLEMENTATION',
      'BASE_IMPLEMENTATION',
      'BASE_PREFS_IMPLEMENTATION',
      'BLINK_COMMON_IMPLEMENTATION',
      'BLINK_IMPLEMENTATION',
      'BLINK_PLATFORM_IMPLEMENTATION',
      'BUILDING_V8_SHARED',
      'CC_IMPLEMENTATION',
      'CC_SURFACES_IMPLEMENTATION',
      'COMPOSITOR_IMPLEMENTATION',
      'CONTENT_IMPLEMENTATION',
      'CRYPTO_IMPLEMENTATION',
      'EVENTS_BASE_IMPLEMENTATION',
      'EVENTS_IMPLEMENTATION',
      'GESTURE_DETECTION_IMPLEMENTATION',
      'GFX_IMPLEMENTATION',
      'GIN_IMPLEMENTATION',
      'GLES2_C_LIB_IMPLEMENTATION',
      'GLES2_IMPL_IMPLEMENTATION',
      'GLES2_UTILS_IMPLEMENTATION',
      'GL_IMPLEMENTATION',
      'GL_IN_PROCESS_CONTEXT_IMPLEMENTATION',
      'GPU_IMPLEMENTATION',
      'HEAP_IMPLEMENTATION',
      'IPC_IMPLEMENTATION',
      'KEYBOARD_IMPLEMENTATION',
      'LIBPROTOBUF_EXPORTS',
      'LIBPROTOC_EXPORTS',
      'MEDIA_IMPLEMENTATION',
      'MESSAGE_CENTER_IMPLEMENTATION',
      'METRO_VIEWER_IMPLEMENTATION',
      'MOJO_COMMON_IMPLEMENTATION',
      'MOJO_ENVIRONMENT_IMPL_IMPLEMENTATION',
      'MOJO_GLES2_IMPLEMENTATION',
      'MOJO_GLES2_IMPL_IMPLEMENTATION',
      'MOJO_NATIVE_VIEWPORT_IMPLEMENTATION',
      'MOJO_SERVICE_MANAGER_IMPLEMENTATION',
      'MOJO_SYSTEM_IMPLEMENTATION',
      'MOJO_SYSTEM_IMPL_IMPLEMENTATION',
      'NATIVE_THEME_IMPLEMENTATION',
      'NET_IMPLEMENTATION',
      'OZONE_IMPLEMENTATION',
      'PPAPI_HOST_IMPLEMENTATION',
      'PPAPI_PROXY_IMPLEMENTATION',
      'PPAPI_SHARED_IMPLEMENTATION',
      'PPAPI_THUNK_IMPLEMENTATION',
      'PRINTING_IMPLEMENTATION',
      'SHELL_DIALOGS_IMPLEMENTATION',
      'SKIA_IMPLEMENTATION',
      'SNAPSHOT_IMPLEMENTATION',
      'SQL_IMPLEMENTATION',
      'SURFACE_IMPLEMENTATION',
      'UI_BASE_IMPLEMENTATION',
      'UI_IMPLEMENTATION',
      'URL_IMPLEMENTATION',
      'U_COMBINED_IMPLEMENTATION_EXCEPT_DATA',
      'U_NO_GLOBAL_NEW_DELETE',
      'U_UTF8_IMPL',
      'V2_IMPLEMENTATION',
      'V8_SHARED',
      'WEBKIT_BASE_IMPLEMENTATION',
      'WEBKIT_CHILD_IMPLEMENTATION',
      'WEBKIT_COMMON_IMPLEMENTATION',
      'WEBKIT_COMPOSITOR_BINDINGS_IMPLEMENTATION',
      'WEBKIT_EXTENSIONS_IMPLEMENTATION',
      'WEBKIT_GLUE_IMPLEMENTATION',
      'WEBKIT_GPU_IMPLEMENTATION',
      'WEBKIT_PLUGINS_IMPLEMENTATION',
      'WEBKIT_RENDERER_IMPLEMENTATION',
      'WEBKIT_STORAGE_BROWSER_IMPLEMENTATION',
      'WEBKIT_STORAGE_COMMON_IMPLEMENTATION',
      'WEBKIT_STORAGE_RENDERER_IMPLEMENTATION',
      'WEBKIT_USER_AGENT_IMPLEMENTATION',
      'WEBORIGIN_IMPLEMENTATION',
      'WTF_IMPLEMENTATION',
    ],
    'chromiumviews_defines': [
      'DISPLAY_IMPLEMENTATION',
      'DISPLAY_UTIL_IMPLEMENTATION',
      'VIEWS_IMPLEMENTATION',
      'WEBVIEW_IMPLEMENTATION',
      'WEB_DIALOGS_IMPLEMENTATION',
      'WM_IMPLEMENTATION',
    ],
  },
  'target_defaults': {
    'defines': [
      '<@(global_defines)',
      '<@(chromiumcontent_defines)',
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
        # Xcode 5.1 doesn't support these flags.
        '-Wno-absolute-value',
        '-Wno-tautological-pointer-compare',
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
          '<@(chromiumcontent_defines)',
        ],
      }],
      ['_target_name in ["views", "webview", "web_dialogs", "wm", "display", "display_util"]', {
        'defines': [
          '<@(chromiumviews_defines)',
        ],
        'defines!': [
          '<@(chromiumcontent_defines)',
        ],
      }],
      ['_target_name in ["v8", "v8_snapshot", "v8_nosnapshot", "v8_external_snapshot", "v8_base", "v8_libbase", "v8_libplatform", "mksnapshot"]', {
        # Override src/v8/build/toolchain.gypi's RuntimeLibrary setting.
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
