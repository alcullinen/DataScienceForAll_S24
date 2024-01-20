test = {
  'name': 'q1_2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> results.num_columns
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> set(['Opponent Name', 'SBCC Score', 'Opponent Score']) == set(results.labels)
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
