{
  'targets': [
    {
      'target_name': 'googletest',
      'type': 'static_library',
      'include_dirs': [
        '.',
        'include',
      ],
      'direct_dependent_settings': {
        'include_dirs': [
          '.',
          'include',
        ],
      },
      'sources': [
        'include/gtest/gtest-death-test.h',
        'include/gtest/gtest-message.h',
        'include/gtest/gtest-param-test.h',
        'include/gtest/gtest-printers.h',
        'include/gtest/gtest-spi.h',
        'include/gtest/gtest-test-part.h',
        'include/gtest/gtest-typed-test.h',
        'include/gtest/gtest.h',
        'include/gtest/gtest_pred_impl.h',
        'include/gtest/gtest_prod.h',
        'include/gtest/internal/gtest-death-test-internal.h',
        'include/gtest/internal/gtest-filepath.h',
        'include/gtest/internal/gtest-internal.h',
        'include/gtest/internal/gtest-linked_ptr.h',
        'include/gtest/internal/gtest-param-util-generated.h',
        'include/gtest/internal/gtest-param-util.h',
        'include/gtest/internal/gtest-port.h',
        'include/gtest/internal/gtest-string.h',
        'include/gtest/internal/gtest-tuple.h',
        'include/gtest/internal/gtest-type-util.h',
        'src/gtest-death-test.cc',
        'src/gtest-filepath.cc',
        'src/gtest-internal-inl.h',
        'src/gtest-port.cc',
        'src/gtest-printers.cc',
        'src/gtest-test-part.cc',
        'src/gtest-typed-test.cc',
        'src/gtest.cc',
        'src/gtest_main.cc',
      ],
    },
    {
      'target_name': 'googletest_bare_essentials',
      'type': 'static_library',
      'include_dirs': [
        '.',
        'include',
      ],
      'direct_dependent_settings': {
        'include_dirs': [
          '.',
          'include',
        ],
      },
      'sources': [
        'src/gtest-all.cc',
        'src/gtest_main.cc',
      ],
    },
  ],
}
