{
  'targets': [
    {
      'target_name': 'chromiumcontent',
      'type': 'shared_library',
      'dependencies': [
        '<(DEPTH)/content/content.gyp:content',
        '<(DEPTH)/content/content.gyp:content_shell_pak',
        'browser_net',
      ], 
      'xcode_settings': {
        'OTHER_LDFLAGS': [
          '-all_load',
        ],
        'LD_DYLIB_INSTALL_NAME': '@rpath/libchromiumcontent.dylib',
      },
    },
    {
      'target_name': 'browser_net',
      'type': 'static_library',
      'sources': [
        '<(DEPTH)/chrome/browser/net/clear_on_exit_policy.cc',
        '<(DEPTH)/chrome/browser/net/clear_on_exit_policy.h',
        '<(DEPTH)/chrome/browser/net/sqlite_persistent_cookie_store.cc',
        '<(DEPTH)/chrome/browser/net/sqlite_persistent_cookie_store.h',
      ],
      'include_dirs': [
        '<(DEPTH)',
      ],
      'xcode_settings': {
        # Export all symbols from this static library even though they aren't
        # specified to be exported in the source code.
        'GCC_INLINES_ARE_PRIVATE_EXTERN': 'NO',
        'GCC_SYMBOLS_PRIVATE_EXTERN': 'NO',
      },
    },
  ],
}
