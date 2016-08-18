{
  'targets': [
    {
      'target_name': 'autofill',
      'type': 'none',
      'dependencies': [
        '<(DEPTH)/components/components.gyp:autofill_core_common',
        '<(DEPTH)/components/components.gyp:autofill_core_browser',
        '<(DEPTH)/components/components.gyp:autofill_server_proto',
        '<(DEPTH)/components/components.gyp:autofill_content_mojo_bindings_mojom',
        '<(DEPTH)/components/components.gyp:autofill_content_mojo_bindings',
        '<(DEPTH)/components/components.gyp:autofill_content_common',
        '<(DEPTH)/components/components.gyp:autofill_content_risk_proto',
        '<(DEPTH)/components/components.gyp:autofill_content_browser',
        '<(DEPTH)/components/components.gyp:autofill_content_renderer',
        '<(DEPTH)/components/components.gyp:data_use_measurement_core',
        '<(DEPTH)/components/components.gyp:os_crypt',
        '<(DEPTH)/components/components.gyp:signin_core_browser',
        '<(DEPTH)/components/components.gyp:signin_core_common',
        '<(DEPTH)/components/components.gyp:webdata_common',
        '<(DEPTH)/third_party/libaddressinput/libaddressinput.gyp:libaddressinput_util',
        '<(DEPTH)/third_party/libphonenumber/libphonenumber.gyp:libphonenumber',
        '<(DEPTH)/third_party/libphonenumber/libphonenumber.gyp:libphonenumber_without_metadata',
      ]
    }
  ]
}
