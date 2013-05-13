{
  'variables': {
    # Chrome turns this off for component builds, and we need to too. Leaving
    # it on would result in both the Debug and Release CRTs being included in
    # the library.
    'win_use_allocator_shim': 0,
  },
  'target_defaults': {
    'defines': [
      'BASE_I18N_IMPLEMENTATION',
      'BASE_IMPLEMENTATION',
      'BASE_PREFS_IMPLEMENTATION',
      'BUILDING_V8_SHARED',
      'CC_IMPLEMENTATION',
      'COMPILER_IMPLEMENTATION',
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
      'U_COMBINED_IMPLEMENTATION_EXCEPT_DATA',
      'U_NO_GLOBAL_NEW_DELETE',
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
    'defines!': [
      'U_STATIC_IMPLEMENTATION',
    ],
    'msvs_disabled_warnings': [
        # class 'std::xx' needs to have dll-interface. Chrome turns this off
        # for component builds, and we need to too.
        4251,
    ],
    'target_conditions': [
      # If WebKit were like all other modules, we'd define both WEBKIT_DLL and
      # WEBKIT_IMPLEMENTATION everywhere so that all symbols would be marked
      # __declspec(dllexport) or __attribute__((visibility("default"))) and
      # thus exported from our shared library. But when WEBKIT_IMPLEMENTATION is
      # defined, WebKit headers include WebCore headers and types, and those
      # headers and types aren't available outside of WebKit, leading to build
      # errors. So instead we define WEBKIT_DLL only when WEBKIT_IMPLEMENTATION
      # is defined. This means that within WebKit symbols will be marked as
      # exported, and outside of WebKit they won't be annotated at all. This
      # works just fine; the linker sees the public definitions and exports the
      # symbols even though the symbols aren't decorated the same way everywhere.
      ['_target_name in ["webcore_prerequisites", "webkit_platform", "webkit", "webkit_wtf_support"]', {
        'defines': [
          'WEBKIT_DLL',
        ],
      }],
    ],
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
    ],
  },
}
