test = {
  'name': 'q1_1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> np.allclose(weird_numbers, np.array([   -2,    12,     3, 15625]), rtol=1e-03, atol=1e-03)
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
