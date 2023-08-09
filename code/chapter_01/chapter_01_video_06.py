########################
### Counting Strings ###
########################

import pandas as pd

aliens = pd.read_csv(
    'data/cosmic_data.csv', 
    engine='pyarrow', 
    dtype_backend='pyarrow'
    )

aliens['art_count'] = aliens['Bio'].str.count(
  'art'
)