test = {
  'name': 'q36',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> SB_markets.num_rows == 5
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> list(SB_markets.column('city')) == ['Santa Barbara', 'Santa Barbara', 'Santa Barbara', 'Santa Barbara', 'Santa Barbara']
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
