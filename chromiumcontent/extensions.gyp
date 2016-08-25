{
  'targets': [
    {
      'target_name': 'extensions',
      'type': 'none',
      'dependencies': [
        '<(DEPTH)/chrome/common/extensions/api/api.gyp:chrome_api',
        '<(DEPTH)/chrome/chrome_resources.gyp:packed_resources',
        '<(DEPTH)/services/shell/shell_public.gyp:shell_public',
        '<(DEPTH)/components/components.gyp:browsing_data',
        '<(DEPTH)/components/components.gyp:content_settings_core_common',
        '<(DEPTH)/components/components.gyp:crx_file',
        '<(DEPTH)/components/components.gyp:guest_view_browser',
        '<(DEPTH)/components/components.gyp:guest_view_common',
        '<(DEPTH)/components/components.gyp:guest_view_renderer',
        '<(DEPTH)/components/components.gyp:json_schema',
        '<(DEPTH)/components/components.gyp:keyed_service_content',
        '<(DEPTH)/components/components.gyp:keyed_service_core',
        '<(DEPTH)/components/components.gyp:policy',
        '<(DEPTH)/components/components.gyp:policy_component_browser',
        '<(DEPTH)/components/components.gyp:policy_component_common',
        '<(DEPTH)/components/components.gyp:pref_registry',
        '<(DEPTH)/components/components.gyp:syncable_prefs',
        '<(DEPTH)/components/components.gyp:ui_zoom',
        '<(DEPTH)/components/components.gyp:url_matcher',
        '<(DEPTH)/components/components.gyp:user_prefs',
        '<(DEPTH)/components/components.gyp:web_cache_browser',
        '<(DEPTH)/components/components.gyp:web_cache_mojo_bindings',
        '<(DEPTH)/components/components.gyp:web_modal',
        '<(DEPTH)/extensions/browser/api/api_registration.gyp:extensions_api_registration',
        '<(DEPTH)/extensions/common/api/api.gyp:extensions_api',
        '<(DEPTH)/extensions/extensions.gyp:extensions_browser',
        '<(DEPTH)/extensions/extensions.gyp:extensions_common',
        '<(DEPTH)/extensions/extensions.gyp:extensions_common_constants',
        '<(DEPTH)/extensions/extensions.gyp:extensions_renderer',
        '<(DEPTH)/extensions/extensions.gyp:extensions_utility',
        '<(DEPTH)/extensions/extensions_resources.gyp:extensions_resources',
        '<(DEPTH)/extensions/extensions_strings.gyp:extensions_strings',
        '<(DEPTH)/third_party/cld_2/cld_2.gyp:cld2_platform_impl',
      ],
      'conditions': [
        ['OS=="win" or OS=="mac"', {
          'dependencies': [
            '<(DEPTH)/components/components.gyp:wifi_component',
          ],
        }]
      ]
    }
  ]
}
