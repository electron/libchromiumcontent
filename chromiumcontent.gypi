{
  'variables': {
    'win_use_allocator_shim': 0,
  },
  'target_defaults': {
    'defines': [
      'BASE_I18N_IMPLEMENTATION',
      'BASE_IMPLEMENTATION',
      'BASE_PREFS_IMPLEMENTATION',
      'BUILDING_V8_SHARED',
      'CC_IMPLEMENTATION',
      'COMPONENT_BUILD',
      'CRYPTO_IMPLEMENTATION',
      'GL_IMPLEMENTATION',
      'GLES2_C_LIB_IMPLEMENTATION',
      'GLES2_IMPL_IMPLEMENTATION',
      'GLES2_UTILS_IMPLEMENTATION',
      'GPU_IMPLEMENTATION',
      'GURL_DLL',
      'GURL_IMPLEMENTATION',
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
      'UI_IMPLEMENTATION',
      'V8_SHARED',
      'WEBKIT_BASE_IMPLEMENTATION',
      'WEBKIT_COMPOSITOR_BINDINGS_IMPLEMENTATION',
      'WEBKIT_GLUE_IMPLEMENTATION',
      'WEBKIT_GPU_IMPLEMENTATION',
      'WEBKIT_PLUGINS_IMPLEMENTATION',
      'WEBKIT_STORAGE_IMPLEMENTATION',
      'WEBKIT_USER_AGENT_IMPLEMENTATION',
    ],
    'msvs_disabled_warnings': [
        4251,
    ],
    'target_conditions': [
      ['_target_name=="base"', {
        # We can't use sources! here because that generates path names relative to this .gypi file, which won't match the relative path names in base.gyp.
        'sources/': [
          ['exclude', 'debug/debug_on_start_win\.cc$'],
        ],
      }],
      ['_target_name in ["libEGL", "libGLESv2"]', {
        'defines': [
          'COMPILER_IMPLEMENTATION',
        ],
      }],
      ['_target_name in ["webcore_prerequisites", "webkit_platform", "webkit", "webkit_wtf_support"]', {
        'defines': [
          'WEBKIT_DLL',
        ],
      }],
      ['_target_name in ["icuuc", "icui18n"]', {
        'defines': [
          'U_OVERRIDE_CXX_ALLOCATION=0',
        ],
      }],
      ['_type=="static_library" and _target_name!="sqlite"', {
        'defines': [
          'U_COMBINED_IMPLEMENTATION',
        ],
        'defines!': [
          'U_STATIC_IMPLEMENTATION',
        ],
      }, {
        'defines': [
          'U_STATIC_IMPLEMENTATION',
        ],
      }],
    ],
  },
}
