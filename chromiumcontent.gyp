{
  'targets': [
    {
      'target_name': 'chromiumcontent',
      'type': 'shared_library',
      'dependencies': [
        '<(DEPTH)/content/content.gyp:content',
        '<(DEPTH)/content/content.gyp:content_shell_pak',
      ], 
      'xcode_settings': {
        'OTHER_LDFLAGS': [
          '-all_load',
        ],
        'LD_DYLIB_INSTALL_NAME': '@rpath/libchromiumcontent.dylib',
      },
    },
  ],
}
