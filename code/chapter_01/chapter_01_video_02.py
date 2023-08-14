#####################
### Testing Speed ###
#####################

import pandas as pd
import pyarrow as pa
import re
import timeit

small_aliens_numpy = pd.read_csv('data/small_cosmic.csv')

small_aliens = pd.read_csv('data/small_cosmic.csv', engine='pyarrow', dtype_backend='pyarrow')

aliens_numpy = pd.read_csv('data/cosmic_data.csv')

aliens = pd.read_csv('data/cosmic_data.csv', engine='pyarrow', dtype_backend='pyarrow')

setup_normal = '''
import pandas as pd
aliens = pd.read_csv('data/cosmic_data.csv')
'''

setup_pyarrow = '''
import pandas as pd
aliens = pd.read_csv('data/cosmic_data.csv', engine='pyarrow', dtype_backend='pyarrow')
'''

statement = '''
aliens['Bio'].str.replace(
  'and',
  '&', 
  regex=True
)
'''

tests = {'setup_normal': setup_normal, 'setup_pyarrow': setup_pyarrow}

for key, value in tests.items():
  times = timeit.repeat(setup=value, 
                        stmt=statement,
                        repeat=2,
                        number=10
                        )
  print('The lowest time for ' + key + ': ', min(times))                      
