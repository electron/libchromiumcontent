{
  'target_defaults': {
    'defines': [
      'BASE_I18N_IMPLEMENTATION',
      'BASE_IMPLEMENTATION',
      'BASE_PREFS_IMPLEMENTATION',
      'BUILDING_V8_SHARED',
      'COMPONENT_BUILD',
      'GLES2_C_LIB_IMPLEMENTATION',
      'GPU_IMPLEMENTATION',
      'GURL_DLL',
      'GURL_IMPLEMENTATION',
      'PPAPI_PROXY_IMPLEMENTATION',
      'SKIA_DLL',
      'SKIA_IMPLEMENTATION',
      'V8_SHARED',
      'WEBKIT_DLL',
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
      ['_type=="static_library"', {
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
