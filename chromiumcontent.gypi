{
  'target_defaults': {
    'defines': [
      'BASE_I18N_IMPLEMENTATION',
      'BASE_IMPLEMENTATION',
      'BASE_PREFS_IMPLEMENTATION',
      'BUILDING_V8_SHARED',
      'COMPONENT_BUILD',
      'COMPILER_IMPLEMENTATION',
      'GPU_IMPLEMENTATION',
      'GURL_DLL',
      'GURL_IMPLEMENTATION',
      'PPAPI_PROXY_IMPLEMENTATION',
      'SKIA_DLL',
      'SKIA_IMPLEMENTATION',
      'U_COMBINED_IMPLEMENTATION',
      'V8_SHARED',
      'WEBKIT_DLL',
    ],
    'defines!': [
      'U_STATIC_IMPLEMENTATION',
    ],
    'target_conditions': [
      ['_target_name=="base"', {
        # We can't use sources! here because that generates path names relative to this .gypi file, which won't match the relative path names in base.gyp.
        'sources/': [
          ['exclude', 'debug/debug_on_start_win\.cc$'],
        ],
      }],
    ],
  },
}
