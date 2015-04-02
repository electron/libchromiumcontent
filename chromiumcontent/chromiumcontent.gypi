{
  'variables': {
    # Enalbe using proprietary codecs.
    'proprietary_codecs': 1,
    'ffmpeg_branding': 'Chrome',
    # And the gold's flags are not available in system's ld neither.
    'linux_use_gold_flags': 0,
    # Make Linux build contain debug symbols, this flag will add '-g' to cflags.
    'linux_dump_symbols': 1,
    # The Linux build of libchromiumcontent.so depends on, but doesn't
    # provide, tcmalloc by default.  Disabling tcmalloc here also prevents
    # any conflicts when linking to binaries or libraries that don't use
    # tcmalloc.
    'linux_use_tcmalloc': 0,
    # Using libc++ requires building for >= 10.7.
    'mac_deployment_target': '10.8',
    # The 10.8 SDK does not work well with C++11.
    'mac_sdk_min': '10.9',
    'conditions': [
      ['OS=="win"', {
        # On Chrome 41 this is disabled on Windows.
        'v8_use_external_startup_data': 1,
        # Chrome turns this off for component builds, and we need to too. Leaving
        # it on would result in both the Debug and Release CRTs being included in
        # the library.
        'win_use_allocator_shim': 0,

        'win_release_RuntimeLibrary': '2', # 2 = /MD (nondebug DLL)
        'win_debug_RuntimeLibrary': '3',   # 3 = /MDd (debug DLL)
      }],
      ['OS=="linux"', {
        # Enable high DPI support on Linux.
        'enable_hidpi': 1,
        # Use Dbus.
        'use_dbus': 1,
      }],
      ['OS=="linux" and host_arch=="ia32"', {
        # Use system installed clang for building.
        'make_clang_dir': '/usr',
        'clang': 1,
        'clang_use_chrome_plugins': 0,
      }],
    ],
  },
  'target_defaults': {
    'msvs_disabled_warnings': [
        # class 'std::xx' needs to have dll-interface. Chrome turns this off
        # for component builds, and we need to too.
        4251,
        # The file contains a character that cannot be represented in these
        # current code page
        4819,
        # no matching operator delete found; memory will not be freed if
        # initialization throws an exception
        4291,
        # non dll-interface class used as base for dll-interface class
        4275,
        # 'GetVersionExW': was declared deprecated
        4996,
    ],
    'xcode_settings': {
      'WARNING_CFLAGS': [
        '-Wno-deprecated-declarations',
      ],
      # Use C++11 library.
      'CLANG_CXX_LIBRARY': 'libc++',  # -stdlib=libc++
    },
    'conditions': [
      ['OS=="linux" and host_arch=="ia32"', {
        'cflags!': [
          # Clang 3.4 doesn't support these flags.
          '-Wno-absolute-value',
          '-Wno-inconsistent-missing-override',
          '-Wno-pointer-bool-conversion',
          '-Wno-tautological-pointer-compare',
          '-Wno-unused-local-typedef',
          '-Wno-undefined-bool-conversion',
          '-Wno-tautological-undefined-compare',
        ],
      }],
    ],
    'target_conditions': [
      ['_target_name in ["nspr", "nss_static"]', {
        'xcode_settings': {
          'GCC_TREAT_WARNINGS_AS_ERRORS': 'NO',
        },
      }],
      ['_target_name=="gtk2ui"', {
        'cflags': [
          '-Wno-sentinel',
        ],
      }],
    ],
  },
}
